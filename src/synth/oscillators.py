import numpy as np


class Oscillator:
    """Luokka, joka vastaa äänen pohjana käytettävien ääniaaltojen generoimisesta

    Attributes:
        freq: taajuus, jonka mukaan värähtelevää aaltoa oskillaattorin tulee
          generoida
        wave: Aaltomuodon valinta
        buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
        samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        old: Tieto edellisen aikadataa sisältävän listan viimeisestä arvosta,
          jota käytetään seuraavan aikadatan luomiseen
    """

    def __init__(self, freq, wave, buffersize, samplerate):
        """Luokan konstruktori, joka alustaa edellämainitut attribuutit.

        Args:
            freq: taajuus, jonka mukaan värähtelevää aaltoa oskillaattorin tulee
              generoida
            wave: Aaltomuodon valinta
            buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
            samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        """

        self.freq = freq
        self.wave = wave
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.old = 0

    def set_wave(self, wave):
        """Metodi, jolla vaihdetaan tarvittaessa oskillaattorin aaltomuoto

        Args:
            wave: Tieto halutusta aaltomuodosta
        """

        self.wave = wave

    def oscillate(self):
        """Metodi, joka luo aikadatan ja kutsuu asianmukaista oskillaattoria

        Returns:
            Palauttaa bufferin koon määrittämän pituisen listan äänidataa sampleina
        """
        time, new = self.generate_time(
            self.old, self.buffersize, self.samplerate)

        if self.wave == 0:
            samples = self.sin_oscillator(self.freq, time)
        elif self.wave == 1:
            samples = self.square_oscillator(self.freq, time)
        elif self.wave == 2:
            samples = self.saw_oscillator(self.freq, time)
        self.old = new
        return samples

    def generate_time(self, old, buffersize, samplerate):
        """Luo aikadatan, jonka pohjalta oskillaattori laskee ääniaallon

        Oskillaattorit laskevat ääniaallot ajan funktioina. Syntetisaattori ei käytä
        aikayksikkönä sekuntia, vaan sampleraten määrittämää sekunnin murto-osaa.

        Args:
            old: Edellisen aikadatalistan päätepiste
            buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
            samplerate: Kuinka moneen sampleen yksi sekunti on jaettu

        Returns:
            time: Metodin generoima lista aikadataa
            new: Tämän luodun listan päätepiste
        """

        new = old + buffersize
        startpoint = old / samplerate
        endpoint = new / samplerate
        time = np.linspace(startpoint, endpoint, buffersize, False)
        return time, new

    def sin_oscillator(self, freq, time):
        """Laskee saamansa ajan pohjalta siniaallon

        Args:
            freq: Laskettavan siniaallon värähtelynopeus
            time: Aika, jonka pohjalta siniaalto lasketaan

        Returns:
            Palauttaa bufferin koon määrittämän pituisen listan äänidataa
            sampleina
        """

        samples = np.sin(freq * 2 * np.pi * time)
        return samples

    def square_oscillator(self, freq, time):
        """laskee saamansa ajan pohjalta kanttiaallon

        args:
            freq: laskettavan kanttiaallon värähtelynopeus
            time: aika, jonka pohjalta kanttiaalto lasketaan

        returns:
            palauttaa bufferin koon määrittämän pituisen listan äänidataa
            sampleina
        """

        attenuate = 0.3
        samples = np.sin(freq * 2 * np.pi * time)
        samples = np.asarray(
            [1 * attenuate if i > 0 else -1 * attenuate for i in samples])
        return samples

    def saw_oscillator(self, freq, time):
        """laskee saamansa ajan pohjalta sahalaita-aallon

        args:
            freq: laskettavan sahalaita-aallon värähtelynopeus
            time: aika, jonka pohjalta sahalaita-aalto lasketaan

        returns:
            palauttaa bufferin koon määrittämän pituisen listan äänidataa
            sampleina
        """
        saw = np.asarray([i * freq - np.floor(i * freq) - 0.5 for i in time])
        return saw
