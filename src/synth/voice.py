from synth.oscillators import Oscillator
from synth.filter import Filter


class Voice:
    """Luokka, joka vastaa yhtä nuottia vastaavan äänen tuottamisesta.

    Luokka ohjaa oskillaatoria luomaan ääniaallon tietyllä taajuudella,
    ja syöttää tämän ääniaallon filtterin läpi. Myöhemmin toivottavasti
    saadaan lisättyä vielä äänenvoimakkuuden vaihtelu nuotin soinnin kuluessa.
    
    Attributes:
        freq: nuotin taajuus, eli korkeus
        wave: äänelle asetettu aaltomuoto, jonka oskillaattori generoi
        buffersize: Kuinka pitkä lista sampleja lasketaan kerralla
        samplerate: Kuinka moneen sampleen yksi sekunti jaetaan
        params: Käyttöliittymän lähettämä, äänen sävyn asetukset
          määrittävä olio
        filter: Filter-luokan olio, joka leikkaa sille syötetystä sample-
          listasta tietyn rajan ylittävät tai alittavat taajuudet pois.
        oscillator: Oscillator-luokan olio, jota käytetään äänen pohjana
          käytettävän ääniaallon generoimiseen.
    """

    def __init__(self, freq, wave, buffersize,
    samplerate, params):
        """Luokan konstruktori, joka alustaa edellä mainitut attribuutit.

        Args:
            freq: Sävelen taajuus, eli korkeus
            wave: Äänen pohjana käytettävän aaltomuodon valinta
            buffersize: Kuinka pitkä lista sampleja lasketaan kerralla
            samplerate: Kuinka moneen sampleen yksi sekunti jaetaan
            params: Käyttöliittymän lähettämä, äänen sävyn asetukset
              määrittävä olio
        """
    
        self.freq = freq
        self.wave = wave
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.params = params
        self.filter = Filter(self.samplerate, self.params.get_cutoff())

        self.oscillator = Oscillator(
            self.freq, self.wave, self.buffersize, self.samplerate)

    def set_parameters(self, params):
        """Päivittää luokan Parameters-olion ajantasaiseksi.

        Jos käyttöliittymässä muutetaan asetuksia, päivitetään ne kaikille
        sillä hetkellä soivillekin sävelille reaaliaikaisesti.

        Args:
            params: Parameters-luokan olio, joka sisältää uudet asetukset. 
        """
        self.wave = params.get_osc()
        self.oscillator.set_wave(self.wave)
        self.filter.set_cutoff(params.get_cutoff())

    def play(self):
        """Luo säveltä vastaavan listan sampleja.

        Luokan päämetodi, jota Synthengine-luokka kutsuu. Generoi ensin 
        Oscillator-luokan oskillaattori-oliolla tietyn taajuuden ääniaallon,
        jonka sitten syöttää filtterin läpi. Tässä implementoidaan tulevaisuudessa
        myös nuotin äänenvoimakkuuden vaihtelu, jos saadaan toimimaan.

        Returns:
            Palauttaa oskillaattorin luoman ja filtterin käsittelemän listan sampleja.
        """
        raw_wave = self.oscillator.oscillate()
        filtered_wave = self.filter.filter(raw_wave)

        return filtered_wave
