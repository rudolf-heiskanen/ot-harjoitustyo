import unittest
from synth.synthengine import Synthengine
from synth.frequencies import calculate_frequencies
from ui.parameters import Parameters

class TestSynthengine(unittest.TestCase):
    def setUp(self):
        self.buffersize = 500
        self.samplerate = 44100
        
        self.engine = Synthengine(self.buffersize, self.samplerate)
    
    # testing intializing
    
    def test_synthengine_parameters_are_correct(self):
        self.assertEqual(self.buffersize, self.engine.buffersize)
        self.assertEqual(self.samplerate, self.engine.samplerate)
        self.assertEqual("poly", self.engine.mode)
        self.assertEqual(1, self.engine.volume)
        self.assertEqual(1, self.engine.oscillator_select)
        self.assertEqual(0, self.engine.clock)
        self.assertEqual((0,0,0), (len(self.engine.pressednotes), len(self.engine.playingnotes), len(self.engine.voices)))

    # testing method play_notes 
    
    def test_frequencies_are_correct(self):
        notes = ['c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3', 'c4']
        self.engine.playingnotes = notes
        self.engine.play_notes()
        
        control_frequencies = calculate_frequencies(notes)
        for i in range(len(control_frequencies)):
            a = control_frequencies[i]
            b = self.engine.voices[i].freq
            
            self.assertEqual(a, b)



    
