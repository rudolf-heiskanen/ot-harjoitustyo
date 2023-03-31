import numpy as np
import pyaudio

class Playbackdevice:
    def __init__(self, buffersize, samplerate):
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.vol = 0.3

        self.stream = pyaudio.PyAudio().open(
            rate=self.samplerate,
            channels=1,
            format=pyaudio.paInt16,
            output=True,
            frames_per_buffer = self.buffersize
        )
    
    def play(self, samples):
        samples *= self.vol * 32767
        samples_as_bytes = np.int16(samples).tobytes()
        self.stream.write(samples_as_bytes)