import pygame
from ui.keypresses import Keyboardinput
from ui.parameters import Parameters
from ui.gui import Gui

class Ui:
    def __init__(self):
        self.keyboardinput = Keyboardinput()
        pygame.init()
        self.params = Parameters()
        self.gui = Gui(self.params)
        self.exit = False
    
    def timed_events(self):
        self.gui_draw()
    
    def check_events(self):
        for event in pygame.event.get():
            self.exit = self.check_for_exit(event)
            self.read_keypresses(event)
            self.check_gui(event)
        
    def check_gui(self, event):
        self.params = self.gui.check_events(event)
    
    def gui_draw(self):
        self.gui.draw()

    def check_for_exit(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        if event.type == pygame.QUIT:
            return True
    
    def get_exit(self):
        return self.exit

    def get_parameters(self):
        return self.params

    def read_keypresses(self, event):
        self.keyboardinput.read_keypresses(event)

    def get_notes(self):
        notes = self.keyboardinput.get_notes()
        return notes
