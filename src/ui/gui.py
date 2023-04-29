import pygame
import pygame_gui

class Gui:
    def __init__(self, params):
        self.h = 800
        self.w = 800
        self.params = params
        self.screen = pygame.display.set_mode((self.h, self.w))
        self.manager = pygame_gui.UIManager((self.h, self.w))

        self.background = pygame.Surface((self.h, self.w))
        self.background.fill(pygame.Color('darkseagreen'))
        self.font = pygame.freetype.SysFont('courier', 22)
        self.smallfont = pygame.freetype.SysFont('courier', 16)

        self.init_gui()

    
    def init_gui(self):
        self.oscillatorbutton_saw = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 100), (100, 50)),
                                                                 text = "Saw",
                                                                 manager=self.manager)

        self.oscillatorbutton_square = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 100), (100, 50)),
                                                                 text = "Square",
                                                                 manager=self.manager)
        
        self.volumeslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((450, 100), (275, 50)),
                                                                   start_value=self.params.volume * 127,
                                                                   value_range=(0,127),
                                                                   manager=self.manager)
        
        self.monobutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 250), (100, 50)),
                                                                                 text = 'Mono',
                                                                                 manager=self.manager)

        self.polybutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 250), (100, 50)),
                                                                                 text = 'Poly',
                                                                                 manager=self.manager)
        
        self.cutoffslider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((450, 250), (275, 50)),
                                                                   start_value= 127 * self.params.cutoff / 20000,
                                                                   value_range=(0,127),
                                                                   manager=self.manager)

    
    def draw_texts(self):
        self.text_oscselect = self.font.render_to(self.screen, (75, 50),'Oscillator select', 'gray33')
        self.text_volume = self.font.render_to(self.screen, (450,50), 'Volume', 'gray33')
        self.text_cutoff = self.font.render_to(self.screen, (450, 200), 'Filter cutoff', 'gray33')

        self.text_volumestart = self.smallfont.render_to(self.screen, (450 ,80), '0', 'white')
        self.text_volumeend = self.smallfont.render_to(self.screen, (695, 80), '127', 'white')
        self.text_cutoffstart = self.smallfont.render_to(self.screen, (450, 230), '0hz', 'white')
        self.text_cutoffend = self.smallfont.render_to(self.screen, (675, 230), '20khz', 'white')

        self.text_polyphony = self.font.render_to(self.screen, (75, 200), 'Polyphony', 'gray33')
    
    def draw_indicators(self):
        if self.params.get_osc() == 2:
            self.saw_indicator = self.font.render_to(self.screen, (75 + (100 / 2) - 3, 85), '¤', 'red')
        if self.params.get_osc() == 1:
            self.square_indicator = self.font.render_to(self.screen, (225 + (100 / 2) -3, 85), '¤', 'red')
        
        if self.params.get_polyphony() == 'mono':
            self.poly_indicator = self.font.render_to(self.screen, (75 + (100 / 2) - 3, 235), '¤', 'red')
        if self.params.get_polyphony() == 'poly':
            self.poly_indicator = self.font.render_to(self.screen, (225 + (100 / 2) -3, 235), '¤', 'red')

    def draw(self):
        self.manager.update(1/1000.0)
        self.screen.blit(self.background, (0,0))
        self.draw_texts()
        self.draw_indicators()
        self.manager.draw_ui(self.screen)
        pygame.display.update()
    
    
    def check_events(self, event):
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
        self.params.set_cutoff(self.cutoffslider.get_current_value() / 127 * 20000 + 1)
        self.manager.process_events(event)

        
        return self.params