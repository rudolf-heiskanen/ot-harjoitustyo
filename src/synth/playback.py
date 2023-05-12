import numpy as np
import pygame


class Playbackdevice:
    """Tämä luokka vastaa äänentoistosta

    Luokka lähettää sille syötetyt samplet pygamen audiokirjastolle,
    joka hoitaa äänen lähettämisen käyttöjärjestelmälle.

    Attributes:
        buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
        samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        vol: Koko sovelluksen maksimiäänenvoimakkuuden säätö
    """

    def __init__(self, buffersize, samplerate):
        """Luokan konstruktori, joka alustaa attribuutit ja pygamen audiojärjestelmän

        Args:
            buffersize: Kuinka monta samplea lasketaan valmiiksi, ennen kuin ne
            samplerate: Kuinka moneen sampleen yksi sekunti on jaettu   
        """
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.vol = 0.3
        pygame.mixer.pre_init(frequency=self.samplerate,
                              size=-16, channels=1, buffer=self.buffersize)

    def play(self, samples):
        """Metodi, joka lähettää saamansa samplet tietylle audiokirjastolle

        Tämä on olemassa sen takia, että kehityksessä on tarvinnut, ja voi
        jatkossakin tarvita vertailla eri audiokirjastojen toimivuutta.

        Args:
            samples: Lista sampleista, jotka sisältävät bufferin koon verran
              äänidataa
        """
        self.play_pygame(samples)

    def play_pygame(self, samples):
        """Metodi hoitaa vaadittavat alkutoimenpiteet ja kutsuu pygamen audiokirjastoa

        Args:
            samples: Lista sampleista, jotka sisältävät bufferin koon verran äänidataa
        """
        if abs(max(samples)) > 1:
            samples *= (1/abs(max(samples)))
        samples *= self.vol
        samples *= 32767
        samples_as_16bit = samples.astype(np.int16)
        sound = pygame.sndarray.make_sound(samples_as_16bit)
        sound.play()
