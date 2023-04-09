import numpy as np
import simpleaudio as sa
import sounddevice as sd
import pygame
import time
from threading import Thread

class Playbackdevice:
    def __init__(self, buffersize, samplerate):
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.vol = 0.3
        #self.mixer = pygame.mixer.pre_init(frequency=self.samplerate,size=-16,channels=1, buffer=self.buffersize)
        pygame.mixer.pre_init(frequency=self.samplerate,size=-16,channels=1, buffer=self.buffersize)
        sd.default.samplerate = self.samplerate
        self.duration = self.buffersize / self.samplerate / 1.05
        self.last = 0

        #self.stream = pyaudio.PyAudio().open(
        #    rate=self.samplerate,
        #    channels=1,
        #    format=pyaudio.paInt16,
        #    output=True,
        #    frames_per_buffer = self.buffersize
        #)
    
    def play(self, samples):
        self.play_pygame(samples)
        #self.play_sounddevice(samples)
        #self.play_simpleaudio(samples)



    def play_pygame(self, samples):
        #self.now = time.time()
        #if self.now - self.last >= self.duration:

        if abs(max(samples)) > 1:
            samples *= (1/abs(max(samples)))
        samples *= self.vol * 32767
        samples_as_16bit = samples.astype(np.int16)
        sound = pygame.sndarray.make_sound(samples_as_16bit)
        sound.play()
        #time.sleep(self.duration)

    def play_sounddevice(self, samples):
        if abs(max(samples)) > 1:
            samples *= (1/abs(max(samples)))
        samples *= self.vol * 32767
        samples_as_16bit = samples.astype(np.int16)
        sd.play(samples_as_16bit, blocking=True)
        time.sleep(self.buffersize / self.samplerate)
        sd.stop()
    
    def play_simpleaudio(self, samples):
        if abs(max(samples)) > 1:
            samples *= (1/abs(max(samples)))
        samples *= self.vol * 32767
        samples_as_16bit = samples.astype(np.int16)
        play_obj = sa.play_buffer(samples_as_16bit, 2, 2, self.samplerate)
        #play_obj.wait_done()
        time.sleep(self.duration)
    
    def mixer_init(self):
        pygame.mixer.quit()
        pygame.mixer.init(frequency=self.samplerate,size=-16,channels=1, buffer=self.buffersize)

