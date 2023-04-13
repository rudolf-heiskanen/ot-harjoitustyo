import unittest
import numpy as np
from synth.oscillators import Oscillator


class TestOscillator(unittest.TestCase):
    def setUp(self):
        self.freq = 300
        self.wave = 0
        self.buffersize = 256
        self.samplerate = 44100
        self.osc = Oscillator(self.freq, self.wave,
                              self.buffersize, self.samplerate)
        self.time = self.osc.generate_time(0, self.buffersize, self.samplerate)[0]


    # testing method oscillate
    
    def test_oscillate_wave_select_0(self):
        oscillator = Oscillator(self.freq, 0, self.buffersize, self.samplerate)
        samples = oscillator.oscillate()
        
        control_samples = oscillator.sin_oscillator(self.freq, self.time)
        
        for i in range(self.buffersize):
            self.assertEqual(samples[i], control_samples[i])
    
    def test_oscillate_wave_select_1(self):
        oscillator = Oscillator(self.freq, 1, self.buffersize, self.samplerate)
        samples = oscillator.oscillate()
        
        control_samples = oscillator.square_oscillator(self.freq, self.time)
        
        for i in range(self.buffersize):
            self.assertEqual(samples[i], control_samples[i])
    
    def test_oscillate_wave_select_2(self):
        oscillator = Oscillator(self.freq, 2, self.buffersize, self.samplerate)
        samples = oscillator.oscillate()
        
        control_samples = oscillator.saw_oscillator(self.freq, self.time)
        
        for i in range(self.buffersize):
            self.assertEqual(samples[i], control_samples[i])
    

    # testing method generate_time

    def test_correct_time_length(self):
        time, new = self.osc.generate_time(0, self.buffersize, self.samplerate)

        self.assertEqual(len(time), self.buffersize)
        self.assertEqual(new, self.buffersize)

    def test_time_generated_correctly(self):
        time, new = self.osc.generate_time(0, self.buffersize, self.samplerate)
        control_time = np.linspace(
            0, self.buffersize / self.samplerate, self.buffersize, False)

        for i in range(0, self.buffersize):
            self.assertEqual(time[i], control_time[i])

            if i > 0:
                step = 1 / 44100
                self.assertAlmostEqual(time[i]-time[i-1], step)


    # testing method sin_oscillator
    
    def test_sin_correct_amplitude_range(self):
        sinewave = self.osc.sin_oscillator(self.freq, self.time)

        self.assertAlmostEqual(max(sinewave), 1, places=2)
        self.assertAlmostEqual(min(sinewave), -1, places=2)

    def test_sin_correct_waveform(self):
        sinewave = self.osc.sin_oscillator(self.freq, self.time)
        control_sinewave = np.sin(self.freq * 2 * np.pi * self.time)

        for i in range(self.buffersize):
            self.assertEqual(sinewave[i], control_sinewave[i])

    
    # testing method square_oscillator

    def test_square_correct_amplitude_range(self):
        squarewave = self.osc.square_oscillator(self.freq, self.time)

        self.assertAlmostEqual(max(squarewave), 0.3, places=2)
        self.assertAlmostEqual(min(squarewave), -0.3, places=2)
    
    def test_square_correct_waveform(self):
        squarewave = self.osc.square_oscillator(self.freq, self.time)
        sinewave = np.sin(self.freq * 2 * np.pi * self.time)
        control_squarewave = np.asarray([0.3 if i > 0 else -0.3 for i in sinewave])
        
        for i in range(self.buffersize):
            self.assertEqual(squarewave[i], control_squarewave[i])

    
    # testing method saw_oscillator
    
    def test_saw_correct_amplitude_range(self):
        sawtoothwave = self.osc.saw_oscillator(self.freq, self.time)
        
        self.assertAlmostEqual(max(sawtoothwave), 0.5, places=1)
        self.assertAlmostEqual(min(sawtoothwave), -0.5, places =1)
    
    def test_saw_correct_waveform(self):
        sawtoothwave = self.osc.saw_oscillator(self.freq, self.time)
        control_sawtoothwave = np.asarray([i * self.freq - np.floor(i * self.freq) - 0.5 for i in self.time])
        
        for i in range(self.buffersize):
            self.assertEqual(sawtoothwave[i], control_sawtoothwave[i])
        
        
