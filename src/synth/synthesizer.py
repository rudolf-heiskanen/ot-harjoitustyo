import pygame
import numpy as np
from time import time
from synth.synthengine import Synthengine
from ui.ui import Ui
from synth.playback import Playbackdevice 

class Synthesizer:
    def __init__(self):
        self.buffersize = 1024
        self.samplerate = 44100
        
        self.duration = self.buffersize / self.samplerate / 1.0
        self.last = 0
        self.clock = 0

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
        self.playbackdevice.mixer_init()
        screen = pygame.display.set_mode((400,400))
        running = True
        samples = self.synthengine.play_notes()

        while running:
            for event in pygame.event.get():
                if self.check_for_exit(event):
                    running = False
                self.ui.read_keypresses(event)
            self.clock = time()
            self.synthengine.get_time(self.clock)

            notes = self.ui.get_notes()
            self.synthengine.register_notes_temporary(notes)

            if self.clock - self.last >= self.duration:
                self.playbackdevice.play(samples)
                samples = self.synthengine.play_notes()
                self.last = self.clock

            
            
