import unittest
from time import time
from synth.synthengine import Synthengine
from synth.frequencies import calculate_frequencies
from ui.parameters import Parameters

class TestSynthengine(unittest.TestCase):
    def setUp(self):
        self.buffersize = 500
        self.samplerate = 44100
        
        self.params = Parameters()
        self.engine = Synthengine(self.buffersize, self.samplerate)
        self.engine.set_parameters(self.params)
    
    # testing intializing
    
    def test_synthengine_parameters_are_correct(self):
        self.assertEqual(self.buffersize, self.engine.buffersize)
        self.assertEqual(self.samplerate, self.engine.samplerate)
        self.assertEqual("poly", self.engine.mode)
        self.assertEqual(1, self.engine.volume)
        self.assertEqual(2, self.engine.oscillator_select)
        self.assertEqual(0, self.engine.clock)
        self.assertEqual((0,0,0), (len(self.engine.pressednotes), len(self.engine.playingnotes), len(self.engine.voices)))
    
    # testing method set_time
    
    def test_set_time(self):
        moment = time()
        self.engine.set_time(moment)

        self.assertEqual(moment, self.engine.clock)

    # testing method play_notes 
    
    def test_frequencies_are_correct_polyphonic(self):
        notes = ['c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3', 'c4']
        self.engine.mode = "poly"
        self.engine.playingnotes = notes
        self.engine.play_notes()
        
        control_frequencies = calculate_frequencies(notes)
        for i in range(len(control_frequencies)):
            a = control_frequencies[i]
            b = self.engine.voices[i].freq
            
            self.assertEqual(a, b)

    def test_frequencies_are_correct_monophonic(self):
        notes = ['c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3', 'c4']
        self.engine.mode = "mono"
        self.engine.playingnotes = notes
        self.engine.play_notes()
        
        control_freq = 261.63
        self.assertEqual(len(self.engine.voices), 1)
        self.assertEqual(self.engine.voices[0].freq, control_freq)
    
    # testing method calculate_voices
    
    def test_calculate_voices_with_preexisting_voices(self):
        notes1 = ['c3', 'd3']
        frequencies1 = self.engine.calculate_frequencies(notes1)
        self.engine.calculate_voices(frequencies1, self.engine.voices)
        
        memory = [voice for voice in self.engine.voices]
        
        notes2 = ['c3', 'd3', 'e3', 'f3']
        frequencies2 = self.engine.calculate_frequencies(notes2)
        self.engine.calculate_voices(frequencies2, self.engine.voices)
        
        self.assertEqual(memory[0], self.engine.voices[0])
        self.assertEqual(memory[1], self.engine.voices[1])
        self.assertEqual(len(self.engine.voices)-len(memory), 2)
    
    def test_calculate_voices_remove_voices(self):
        notes = ['c3', 'd3', 'e3', 'f3']
        frequencies = self.engine.calculate_frequencies(notes)
        voices = self.engine.calculate_voices(frequencies, self.engine.voices)
        self.assertEqual(len(voices), 4)

        notes = []
        frequencies = self.engine.calculate_frequencies(notes)
        print(frequencies)
        voices = self.engine.calculate_voices(frequencies, self.engine.voices)
        print(voices)
        print([voice.freq for voice in voices])
        