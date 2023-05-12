import pygame
from ui.keypresses import Keyboardinput
from ui.parameters import Parameters
from ui.gui import Gui


class Ui:
    """Luokka, joka hallinnoi näppäimistöinputin ja graafisen käyttöliittymän informaation käsittelyä
    
    Luokkaa kutsutaan säännöllisesti ohjelman pääloopista näppäimistöinputin
    ja graafisen käyttöliittymän tilan tarkistamiseksi.
    
    Attributes:
        keyboardinput: Luokan, joka tarkistaa näppäimistön painallukset, instanssi
        params: Luokan, joka säilyttää graafisen käyttöliittymän asetukset, instanssi
        gui: Luokan, joka hoitaa graafisen käyttöliittymän piirtämisen ja lukemisen, instanssi
        exit: Tieto siitä, onko näppäimistön tai graafisen käyttöliittymän kautta tullut
          käsky sulkea ohjelma. Attribuutin arvo on joko True tai False
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa edellä luetellut attribuutit
        """

        self.keyboardinput = Keyboardinput()
        pygame.init()
        self.params = Parameters()
        self.gui = Gui(self.params)
        self.exit = False

    def timed_events(self):
        """Metodi, jota kutsutaan synthesizer-luokalle määritellyn bufferin koon määrittämin intervallein
        
        Metodin sisään on koottu kaikki toiminnot, jotka tarvitsee suorittaa vain tietyin väliajoin,
        eikä jokaisella pääloopin kierroksella.
        """

        self.gui_draw()

    def check_events(self):
        """Metodi, joka tarkistaa pygame-eventit, eli käytännössä inputin.

        Tätä metodia kutsutaan jokaisella pääloopin suorituskerralla.
        """

        for event in pygame.event.get():
            self.exit = self.check_for_exit(event)
            self.read_keypresses(event)
            self.check_gui(event)

    def check_gui(self, event):
        """Metodi, joka lukee graafisen käyttöliittymän tilan.
        """

        self.params = self.gui.check_events(event)

    def gui_draw(self):
        """Metodi, joka kutsuu gui-oliota piirtämään uudelleen graafisen käyttöliittymän tilan.
        """

        self.gui.draw()

    def check_for_exit(self, event):
        """Metodi, joka tarkistaa, onko näppäimistöltä tai graafiselta käyttöliittymältä tullut poistumiskäsky.
        
        Args:
            event: pygame-eventti, josta tarkistetaan, onko se poistumiskäsky.
        
        Returns:
            Palauttaa tiedon, oliko argumenttina annettu event poistumiskäsky. Tieto on bool-tyyppiä.
        """
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        if event.type == pygame.QUIT:
            return True

    def get_exit(self):
        """Metodi, joka palauttaa pääohjelmalle, tiedon, onko poistumiskäsky annettu.

        Returns:
            Palauttaa tiedon, onko poistumiskäsky annettu. Tieto on bool-tyyppiä.
        """

        return self.exit

    def get_parameters(self):
        """Metodi, joka palauttaa pääohjelmalle graafisen käyttöliittymän tilan.
        
        Returns:
            Palauttaa graafisen käyttöliittymän tilan Parameters-luokan oliona.
        """

        return self.params


    def read_keypresses(self, event):
        """Metodi, joka lukee näppäimistön painallukset.

        Args:
            event: pygame-eventti, joka sisältää tiedon näppäimen painalluksesta.
        """

        self.keyboardinput.read_keypresses(event)

    def get_notes(self):
        """Metodi, joka palauttaa pääohjelmalle tällä hetkellä painetut nuotit.

        Returns:
            Palauttaa tällä hetkellä painetut nuotit listana.
        """
        notes = self.keyboardinput.get_notes()
        return notes
