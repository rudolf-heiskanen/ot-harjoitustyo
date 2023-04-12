import numpy as np
import pygame


class Playbackdevice:
    def __init__(self, buffersize, samplerate):
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.vol = 0.3
        pygame.mixer.pre_init(frequency=self.samplerate,
                              size=-16, channels=1, buffer=self.buffersize)
        self.duration = self.buffersize / self.samplerate / 1.05
        self.last = 0

    def play(self, samples):
        self.play_pygame(samples)

    def play_pygame(self, samples):
        samples *= self.vol
        if abs(max(samples)) > 1:
            samples *= (1/abs(max(samples)))
        samples *= 32767
        samples_as_16bit = samples.astype(np.int16)
        sound = pygame.sndarray.make_sound(samples_as_16bit)
        sound.play()
