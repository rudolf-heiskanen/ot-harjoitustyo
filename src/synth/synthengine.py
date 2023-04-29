import numpy as np
from synth.voice import Voice
from synth.frequencies import calculate_frequencies


class Synthengine:
    """Luokka joka hallinnoi nuottidatan muuttamista ääneksi
    
    Luokka saa Synthesizer-luokan välittämänä tiedon painetuista nuoteista,
    laskee mitä frekvenssiä kukin nuotti vastaa, ja luo tämän tiedon
    perusteella Voice-luokan instanssit jotka vastaavat kukin yhden nuotin
    äänen generoimisesta.
    
    Attributes:
        pressednotes: Lista nuoteista, jotka käyttöliittymä on ilmoittanut painetuiksi
        playingnotes: Lista nuoteista, jotka soivat (ml. ne, joiden näppäin on jo
          vapautettu) (tulevaa toiminnallisuutta)
        voices: Lista Voice-olioista, jotka vastaavat playingnotes-listan
          nuottien muuntamisesta ääneksi
        oscillator_select: Äänen aaltomuodon valinta
        samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
          lähetetään äänentoistosta vastaavalle osalle
        mode: Moniäänisyyden valinta
        clock: Kello (saatetaan käyttää tulevassa toiminnallisuudessa)
        volume: Äänenvoimakkuus
        params: Tähän asetetaan myöhemmin Parameters-luokan olio, jota käytetään
          äänen asetusten välittämiseen käyttöliittymältä sovelluslogiikalle.
    """

    def __init__(self, buffersize, samplerate):
        """Luokan konstruktorimetodi

        Args:
            buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
              lähetetään äänentoistosta vastaavalle osalle
            samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        """

        self.pressednotes = []
        self.playingnotes = []
        self.voices = []
        self.oscillator_select = 1
        self.samplerate = samplerate
        self.buffersize = buffersize
        self.mode = "poly"
        self.clock = 0
        self.volume = 1
        self.params = False

    def set_time(self, clock):
        """Asettaa luokan kellon. Otetaan mahdollisesti käyttöön tulevassa toiminnallisuudessa.
        
        Args:
            clock: Kellon arvo, joka asetetaan luokan attribuutille
        """
        
        self.clock = clock

    def set_parameters(self, params):
        """Asettaa luokan params-attribuutille Parameters-olion.

        Parameters-olio sisältää äänen asetuksia, joita voi säätää käyttöliittymällä.
        
        Args:
            params: Parameters-luokan olio.
        """
        self.params = params
        for voice in self.voices:
            voice.set_parameters(params)
        self.oscillator_select = params.get_osc()
        self.volume = params.get_volume()
        self.mode = params.get_polyphony()

    def play_notes(self):
        """Hallinnoi nuottien muuttamista nuottidatasta ääneksi.

        Luokan tärkein metodi, jota Synthesizer-luokan päälooppi kutsuu.
        
        Returns:
            Palauttaa buffersizen määrittämän pituisen listan sampleja, jotka
            äänentoistosta vastaava osa osaa soittaa äänenä kaiuttimista.
        """
        
        frequencies = self.calculate_frequencies(self.playingnotes)
        self.voices = self.calculate_voices(frequencies, self.voices)
        samples_list = [voice.play() for voice in self.voices]
        samples = self.sum_samples(samples_list)
        return samples

    def register_notes_temporary(self, notes: list):
        """Kirjaa luokan attribuuttiin tiedon siitä, mitkä nuotit ovat painettuina.
         
        Metodi on vielä keskeneräinen, tulevassa toiminnallisuudessa voi toivottavasti
        asettaa äänen hiipumaan hitaasti näppäimestä irti päästämisen jälkeen. Tämä luultavasti
        laskettaisiin tässä vaiheessa.

        Args:
            notes: Lista painetuista nuoteista.
        """

        self.pressednotes = notes
        self.release_times_temporary()

    def mode_select(self):
        """Tekee tarvittavat moniäänisyyttä koskevat toimenpiteet luokan playingnotes-attribuutista haetulle listalle nuotteja.
        
        Returns:
            Palauttaa listan nuotteja, joissa on otettu huomioon moniäänisyysasetus.
        """
        self.playingnotes.sort()
        if self.mode == "mono":
            if len(self.playingnotes) > 0:
                notes = [self.playingnotes.pop()]
            else:
                notes = []
        return notes

    def release_times_temporary(self):
        """Tämäkin metodi on keskeneräinen ja liittyy tulevaan toiminnallisuudeen äänen hiipumisesta irti päästön jälkeen.
        """

        self.playingnotes = self.pressednotes

    def calculate_frequencies(self, notes):
        """Laskee nuottidatan pohjalta ne taajuudet tai frekvenssit, joita nuottien nimet vastaavat.

        Args:
            notes: Lista nuoteista, jotka tulee muuttaa vastaaviksi taajuuksiksi.

        Returns:
            Palauttaa saamaansa nuottilistaa vastaavan listan taajuuksia.
        """

        frequencies = calculate_frequencies(notes)

        if self.mode == "mono":
            if len(frequencies) > 0:
                frequencies = [frequencies.pop()]
        elif self.mode == "poly":
            pass
        return frequencies

    def calculate_voices(self, frequencies, voices_old):
        """Laskee vastaavat Voice-oliot kullekin soivalle taajuudelle.

        Tarkistaa ensin, onko taajuutta vastaava Voice-olio jo olemassa, ja jos ei ole,
        luo uuden antaen oliolle parametreiksi kyseisen taajuuden ja Parameters-olion,
        joka sisältää äänen väriä koskevat asetukset.

        Args:
            frequencies: Lista taajuuksista, joita vastaavat Voice-oliot tulee olla olemassa
            voices_old: Lista jo tällä hetkellä olemassa olevista Voice-olioista
        
        Returns:
            Palauttaa päivitetyn listan Voice-olioista.
        """
        voices = voices_old
        for frequency in frequencies:
            found = False
            for voice in voices:
                if voice.freq == frequency:
                    found = True
            if not found:
                voices.append(
                    Voice(frequency, self.oscillator_select, self.buffersize,
                    self.samplerate, self.params))

        for voice in voices:
            if voice.freq not in frequencies:
                voices.remove(voice)

        return voices

    def sum_samples(self, samples_list):
        """Laskee yhteen eri sävelten samplet yhdeksi listaksi.

        Metodi laskee Voice-olioiden jokaiselle sävelelle luomat sample-listat 
        yhteen yhdeksi listaksi, jonka äänentoistosta vastaava osa pystyy toistamaan.

        Args:
            samples_list: Lista jokaista soivaa säveltä vastaavista sampleista

        Returns:
            Palauttaa yhteenlasketun listan eri sävelten sampleista.

        """

        blank = np.asarray([0.0*256])
        samples_list.append(blank)
        samples = sum(samples_list)
        samples *= self.volume
        return samples
