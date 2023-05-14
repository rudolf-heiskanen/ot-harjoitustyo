import pygame
import pygame_gui


class Gui:
    """Luokka, joka piirtää ja lukee graafisen käyttöliittymän.
    
    Attributes:
        h: pygame-ikkunan korkeus
        w: pygame-ikkunan leveys
        params: Parameters-luokan olio, jota käytetään graafisen käyttöliittymän tietojen välittämiseen
        screen: pygamen näyttö-olio
        manager: pygame_gui-kirjaston ui-hallinnointi-olio
        background: ikkunan taustavärin kantava pygamen surface-olio
        font: pygamen fonttiolio, jota kutsumalla näytölle voi piirtää tekstiä
        smallfont: pienemmällä kirjasinkoolla varustettu pygamen fonttiolio
    """

    def __init__(self, params):
        """Luokan konstruktori

        Args:
            params: Parameters-luokan olio, jota käytetään graafisen käyttöliittymän tietojen välittämiseen
        """

        self.h = 800
        self.w = 800
        self.params = params
        self.screen = pygame.display.set_mode((self.h, self.w))
        pygame.display.set_caption('SyntsaSyntikka')
        self.manager = pygame_gui.UIManager((self.h, self.w))

        self.background = pygame.Surface((self.h, self.w))
        self.background.fill(pygame.Color('darkseagreen'))
        self.font = pygame.freetype.SysFont('courier', 22)
        self.smallfont = pygame.freetype.SysFont('courier', 16)

        self.init_gui()

    def init_gui(self):
        """Metodi, joka luo graafisen käyttöliittymän liukusäätimet ja painikkeet
        """

        self.oscillatorbutton_saw = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 100), (100, 50)),
                                                                 text="Saw",
                                                                 manager=self.manager)

        self.oscillatorbutton_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 100), (100, 50)),
                                                                    text="Square",
                                                                    manager=self.manager)

        self.volumeslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((450, 100), (275, 50)),
                                                                   start_value=self.params.volume * 127,
                                                                   value_range=(
                                                                       0, 127),
                                                                   manager=self.manager)

        self.monobutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 250), (100, 50)),
                                                       text='Mono',
                                                       manager=self.manager)

        self.polybutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 250), (100, 50)),
                                                       text='Poly',
                                                       manager=self.manager)

        self.cutoffslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((450, 250), (275, 50)),
                                                                   start_value=127 * self.params.cutoff / 20000,
                                                                   value_range=(
                                                                       0, 127),
                                                                   manager=self.manager)
    
    def draw_instructions(self):
        """Metodi, joka piirtää näytölle ohjeet soittimen soittamiseen
        """

        self.text_instructions_1 = self.font.render_to(
            self.screen, (40, 400), 'Ohjeet:' 
        )
        self.text_instructions_2 = self.smallfont.render_to(
            self.screen, (40, 430), 'Voit soittaa syntetisaattoria tietokoneesi näppäimistöllä' 
        )
        self.text_instructions_3 = self.smallfont.render_to(
            self.screen, (40, 455), 'Koskettimet on sijoitettu näppäimistölle seuraavaan tapaan:' 
        )
        self.text_instructions_4 = self.smallfont.render_to(
            self.screen, (40, 480), ' W E    T Y U' 
        )
        self.text_instructions_5 = self.smallfont.render_to(
            self.screen, (40, 505), 'A S D F G H J K L' 
        )
        self.text_instructions_6 = self.smallfont.render_to(
            self.screen, (40, 530), 'Jossa alempi rivi on valkoiset koskettimet, ja ylempi mustat koskettimet.' 
        )
        self.text_instructions_7 = self.smallfont.render_to(
            self.screen, (40, 555), 'Käytössä on siis yksi oktaavi C:stä H:hon ja vielä seuraavan oktaavin C.' 
        )
        self.text_instructions_8 = self.smallfont.render_to(
            self.screen, (40, 580), '' 
        )
        self.text_instructions_9 = self.smallfont.render_to(
            self.screen, (40, 605), 'Graafisella käyttöliittymällä voit valita oskillaattorin aaltomuodon,' 
        )
        self.text_instructions_10 = self.smallfont.render_to(
            self.screen, (40, 630), 'soittimen moniäänisyyden, filtterin leikkausfrekvenssin' 
        )
        self.text_instructions_11 = self.smallfont.render_to(
            self.screen, (40, 655), 'ja soittimen äänenvoimakkuuden.' 
        )
        self.text_instructions_12 = self.smallfont.render_to(
            self.screen, (40, 680), '' 
        )
        self.text_instructions_13 = self.smallfont.render_to(
            self.screen, (40, 705), 'Jos ääni pätkii merkittävästi, käynnistä ohjelma uudestaan.'
        )


    def draw_texts(self):
        """Metodi, joka piirtää liukusäädinten ja painikkeiden otsikkotekstit ja muut näihin liittyvät tekstit
        """

        self.text_oscselect = self.font.render_to(
            self.screen, (75, 50), 'Oscillator select', 'gray33')
        self.text_volume = self.font.render_to(
            self.screen, (450, 50), 'Volume', 'gray33')
        self.text_cutoff = self.font.render_to(
            self.screen, (450, 200), 'Filter cutoff', 'gray33')

        self.text_volumestart = self.smallfont.render_to(
            self.screen, (450, 80), '0', 'white')
        self.text_volumeend = self.smallfont.render_to(
            self.screen, (695, 80), '127', 'white')
        self.text_cutoffstart = self.smallfont.render_to(
            self.screen, (450, 230), '0hz', 'white')
        self.text_cutoffend = self.smallfont.render_to(
            self.screen, (675, 230), '20khz', 'white')

        self.text_polyphony = self.font.render_to(
            self.screen, (75, 200), 'Polyphony', 'gray33')
        
        self.draw_instructions()


    def draw_indicators(self):
        """Metodi, joka piirtää indikaattorit, jotka osoittavat mikä vaihtoehto on valittuna
        
        Tällaiset indikaattorit ovat moniäänisyyden ja oskillaattorin aaltomuotoa koskevien
        painikkeiden yläpuolella, ja ne osoittavat, kumpi kahdesta valittavasta vaihtoehdosta
        on tällä hetkellä käytössä.
        """
        
        if self.params.get_osc() == 2:
            self.saw_indicator = self.font.render_to(
                self.screen, (75 + (100 / 2) - 3, 85), '¤', 'red')
        if self.params.get_osc() == 1:
            self.square_indicator = self.font.render_to(
                self.screen, (225 + (100 / 2) - 3, 85), '¤', 'red')

        if self.params.get_polyphony() == 'mono':
            self.poly_indicator = self.font.render_to(
                self.screen, (75 + (100 / 2) - 3, 235), '¤', 'red')
        if self.params.get_polyphony() == 'poly':
            self.poly_indicator = self.font.render_to(
                self.screen, (225 + (100 / 2) - 3, 235), '¤', 'red')

    def draw(self):
        """Metodi, joka kutsuu yksittäisestä elementistä vastaavia piirtämismetodeita

        Luokalla on metodit, kullekin piirrettävälle "elementtityypille" joita näytölle piirretään,
        ja tällä metodilla pystyy kutsumaan ne kaikki kätevästi kerralla.
        """

        self.manager.update(1/1000.0)
        self.screen.blit(self.background, (0, 0))
        self.draw_texts()
        self.draw_indicators()
        self.manager.draw_ui(self.screen)
        pygame.display.update()

    def check_events(self, event):
        """Metodi, joka tarkistaa gui:n liukusäädinten ja painikkeiden tilan
        
        Args:
            event: pygame-eventti, joka on mahdollisesti informaatiota gui:n liukusäätimen tai
              painikkeen uudesta tilasta
        
        Returns:
            palauttaa Parameters-luokan olion, joka kantaa tämänhetkistä gui:n liukusäädinten
              ja painikkeiden tilaa.
        """

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.oscillatorbutton_saw:
                self.params.set_osc("saw")
            elif event.ui_element == self.oscillatorbutton_square:
                self.params.set_osc("square")
            elif event.ui_element == self.monobutton:
                self.params.set_polyphony("mono")
            elif event.ui_element == self.polybutton:
                self.params.set_polyphony("poly")

        self.params.set_volume(self.volumeslider.get_current_value() / 127)
        self.params.set_cutoff(
            self.cutoffslider.get_current_value() / 127 * 20000 + 1)
        self.manager.process_events(event)

        return self.params
