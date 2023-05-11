import unittest
from synth.voice import Voice
from synth.oscillators import Oscillator
from synth.filter import Filter
from ui.parameters import Parameters

class TestVoice(unittest.TestCase):
    def setUp(self):
        self.freq = 300
        self.wave = 2
        self.buffersize = 200
        self.samplerate = 44100
        self.params = Parameters()
        
        self.voice = Voice(self.freq, self.wave, self.buffersize, self.samplerate, self.params)

    # testing intializing

    def test_voice_parameters_are_correct(self):
        self.assertEqual(self.voice.freq, self.freq)
        self.assertEqual(self.voice.wave, self.wave)
        self.assertEqual(self.voice.buffersize, self.buffersize)
        self.assertEqual(self.voice.samplerate, self.samplerate)
    
    # testing method set_parameters

    def test_set_parameters(self):
        testparams = Parameters()
        testparams.set_osc("square")
        
        self.voice.set_parameters(testparams)
        self.assertEqual(self.voice.wave, 1)
    
    # testing method play

    def test_play(self):
        filter = Filter(self.samplerate, self.params.get_cutoff())
        control_osc = Oscillator(self.freq, self.wave, self.buffersize, self.samplerate)
        control_samples = control_osc.oscillate()
        control_samples = filter.filter(control_samples)
        samples = self.voice.play()
        
        for i in range(len(control_samples)):
            self.assertEqual(control_samples[i], samples[i])

        
    

