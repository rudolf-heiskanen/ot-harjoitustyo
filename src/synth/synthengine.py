from synth.oscillators import Oscillator
from synth.voice import Voice
import numpy as np

class Synthengine:
    def __init__(self, buffersize, samplerate):
        self.pressednotes = []
        self.playingnotes = []
        self.voices = []
        self.oscillator_select = 1
        self.samplerate = samplerate
        self.buffersize = buffersize
        self.mode = "mono"


    def play_notes(self):
        notes = self.mode_select()
        frequencies = self.calculate_frequencies(notes)
        self.oscillators = self.calculate_voices(frequencies, self.voices)
        samples_list = [voice.play() for voice in self.voices]
        samples = self.sum_samples_temp(samples_list)
        return samples
        

    def register_notes_temporary(self, notes: list):
        self.pressednotes = notes
        self.release_times_temporary()

    def mode_select(self):
        if self.mode == "mono":
            if len(self.playingnotes) > 0:
                notes = [self.playingnotes.pop()]
            else:
                notes = []
        else:
            pass
        return notes

    def release_times_temporary(self):
        self.playingnotes = self.pressednotes

    def calculate_frequencies(self, notes):
        frequencies = []
        for note in notes:
            if note == "c3":
                frequencies.append(130.81)
        return frequencies
    
    def calculate_voices(self, frequencies, voices_old):
        voices = voices_old
        for frequency in frequencies:
            found = False
            for voice in voices:
                if voice.freq == frequency:
                    found = True
            if not found:
                voices.append(Voice(frequency, self.oscillator_select, self.buffersize, self.samplerate))
        
        for voice in voices:
            if voice.freq not in frequencies:
                voices.remove(voice)
        
        return voices
    
    def sum_samples_temp(self, samples_list):
        if len(samples_list) == 0:
            lista = [0.0 for i in range(256)]
            return np.asarray(lista)
        else:
            return samples_list[0]
        return samples

    def sum_samples(self, samples_list):
        blank = np.asarray([0.0*256])
        samples_list.append(blank)
        samples = sum(samples_list)
        return samples