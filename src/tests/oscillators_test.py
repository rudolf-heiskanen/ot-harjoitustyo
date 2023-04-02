import unittest
import numpy as np
from synth.oscillators import Oscillator

class TestOscillator(unittest.TestCase):
    def setUp(self):
        self.freq = 300
        self.wave = 0
        self.buffersize = 256
        self.samplerate = 44100
        self.osc = Oscillator(self.freq, self.wave, self.buffersize, self.samplerate)
    
    #testing method generate_time

    def test_correct_time_length(self):
        time, new = self.osc.generate_time(0, self.buffersize, self.samplerate)

        self.assertEqual(len(time), self.buffersize)
        self.assertEqual(new, self.buffersize)
    
    def test_time_generated_correctly(self):
        time, new = self.osc.generate_time(0, self.buffersize, self.samplerate)
        control_time = np.linspace(0, self.buffersize / self.samplerate, self.buffersize, False)

        for i in range(0,self.buffersize):
            self.assertEqual(time[i], control_time[i])
            
            if i > 0:
                step = 1 / 44100
                self.assertAlmostEqual(time[i]-time[i-1], step)


    
            