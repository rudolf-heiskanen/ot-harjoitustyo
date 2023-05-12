import scipy


class Filter:
    """Luokka, joka filtteröi annetusta äänidatasta tiettyjä taajuuksia pois

    Filtteri karkeasti sanottuna leikkaa pois joko cutoffin ala- tai yläpuoliset
    taajuudet äänidatasta.

    Attributes:
        samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        cutoff: Raja, jonka ala- tai yläpuolelta filtteri leikkaa taajuuksia
        mode: Tieto siitä, päästääkö fitteri leikkaamattomina läpi matalat
          taajuudet (low pass) vai korkeat taajuudet (high pass)
    """

    def __init__(self, samplerate, cutoff):
        """Luokan konstruktori, joka alustaa edellä mainitut attribuutit.

        Args:
            samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
            cutoff: Raja, jonka ala- tai yläpuolelta filtteri leikkaa taajuuksia
        """

        self.samplerate = samplerate
        self.cutoff = cutoff
        self.mode = "lowpass"

    def filter(self, samples):
        """Metodi, joka suorittaa itse filtteröinnin

        Args: 
            samples: Lista audiodataa sampleina

        Returns:
            Palauttaa listan audiodataa sampleina, jolle on suoritettu filtteröinti
        """

        filter_b, filter_a = scipy.signal.iirfilter(4, Wn=self.cutoff,
                                                    fs=self.samplerate, btype="low", ftype="butter")
        samples_filtered = scipy.signal.lfilter(filter_b, filter_a, samples)
        return samples_filtered

    def set_cutoff(self, cutoff):
        """Metodi, jolla voi asettaa cutoffille uuden arvon

        Args:
            cutoff: Uusi arvo cutoffille
        """

        self.cutoff = cutoff
