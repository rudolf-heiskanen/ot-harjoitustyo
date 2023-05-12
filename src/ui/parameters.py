class Parameters:
    """Luokka, joka vastaa graafisella käyttöliittymällä muokattavien asetusten välittämisestä
    
    Attributes:
        osc: aaltomuodon valinta
        polyphony: moniäänisyyden valinta
        volume: äänenvoimakkuuden kerroin
        cutoff: filtterin leikkaustaajuus hertseinä
    """

    def __init__(self):
        """Luokan konstruktori
        """

        self.osc = 2
        self.polyphony = "poly"
        self.volume = 1
        self.cutoff = 20000

    def get_osc(self):
        """Metodi, jolla haetaan aaltomuodon valinta
        
        Returns:
            Palauttaa tiedon siitä, mikä aaltomuoto on valittuna.
        """

        return self.osc

    def set_osc(self, mode):
        """Metodi, jolla asetetaan aaltomuodon valinta
        
        Args:
            mode: haluttu aaltomuoto
        """

        if mode == "saw":
            self.osc = 2
        if mode == "square":
            self.osc = 1

    def get_volume(self):
        """Metodi, jolla haetaan äänenvoimakkuuden kerroin
        
        Returns:
            Palauttaa tämänhetkisen äänenvoimakkuuden kertoimen
        """

        return self.volume

    def set_volume(self, vol):
        """Metodi, jolla asetetaan äänenvoimakkuuden kerroin
        
        Args:
            vol: haluttu uusi äänenvoimakkuuden kerroin
        """

        self.volume = vol

    def get_polyphony(self):
        """Metodi, jolla haetaan tieto moniäänisyydestä
        
        Returns:
            palauttaa tiedon moniäänisyydestä
        """

        return self.polyphony

    def set_polyphony(self, polyphony):
        """Metodi, jolla asetetaan uusi tieto moniäänisyydestä

        Args:
            polyphony: sisältää uuden tiedon moniäänisyydestä
        """

        self.polyphony = polyphony

    def get_cutoff(self):
        """Metodi, jolla haetaan tieto filtterin leikkauskohdasta
        
        Returns:
            Palauttaa filtterin leikkauskohdan hertseinä
        """

        return self.cutoff

    def set_cutoff(self, cutoff):
        """Metodi, jolla asetetaan uusi filtterin leikkauskohta
        
        Args:
            cutoff: uusi filtterin leikkauskohta hertseinä
        """

        self.cutoff = cutoff
