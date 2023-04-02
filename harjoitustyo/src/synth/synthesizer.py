import pygame
import numpy as np
from time import time
from synth.synthengine import Synthengine
from ui.ui import Ui
from synth.playback import Playbackdevice 

class Synthesizer:
    def __init__(self):
        self.buffersize = 4096
        self.samplerate = 44100

        self.synthengine = Synthengine(self.buffersize, self.samplerate)
        self.ui = Ui()
        self.playbackdevice = Playbackdevice(self.buffersize, self.samplerate)

    def check_for_exit(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        return False
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((400,400))
        running = True

        while running:
            for event in pygame.event.get():
                if self.check_for_exit(event):
                    running = False
                self.ui.read_keypresses_temporary(event)

            notes = self.ui.get_notes()
            self.synthengine.register_notes_temporary(notes)
            samples = self.synthengine.play_notes()
            self.playbackdevice.play(samples)

            
            
