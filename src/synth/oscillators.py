import numpy as np


class Oscillator:
    def __init__(self, freq, wave, buffersize, samplerate):
        self.freq = freq
        self.wave = wave
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.old = 0

    def oscillate(self):
        time, new = self.generate_time(
            self.old, self.buffersize, self.samplerate)

        if self.wave == 0:
            samples = self.sin_oscillator(self.freq, time)
        elif self.wave == 1:
            samples = self.square_oscillator(self.freq, time)
        elif self.wave == 2:
            samples = self.saw_oscillator(self.freq, time)
        self.old = new
        return samples

    def generate_time(self, old, buffersize, samplerate):
        new = old + buffersize
        startpoint = old / samplerate
        endpoint = new / samplerate
        time = np.linspace(startpoint, endpoint, buffersize, False)
        return time, new

    def sin_oscillator(self, freq, time):
        samples = np.sin(freq * 2 * np.pi * time)
        return samples

    def square_oscillator(self, freq, time):
        attenuate = 0.3
        samples = np.sin(freq * 2 * np.pi * time)
        samples = np.asarray(
            [1 * attenuate if i > 0 else -1 * attenuate for i in samples])
        return samples

    def saw_oscillator(self, freq, time):
        saw = np.asarray([i * freq - np.floor(i * freq) - 0.5 for i in time])
        return saw
