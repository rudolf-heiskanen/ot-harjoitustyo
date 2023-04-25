import numpy as np
from synth.voice import Voice
from synth.frequencies import calculate_frequencies


class Synthengine:
    def __init__(self, buffersize, samplerate):
        self.pressednotes = []
        self.playingnotes = []
        self.voices = []
        self.oscillator_select = 1
        self.samplerate = samplerate
        self.buffersize = buffersize
        self.mode = "poly"
        self.clock = 0
        self.volume = 1

    def set_time(self, clock):
        self.clock = clock

    def set_parameters(self, params):
        for voice in self.voices:
            voice.set_parameters(params)
        self.oscillator_select = params.get_osc()
        self.volume = params.get_volume()
        self.mode = params.get_polyphony()

    def play_notes(self):
        frequencies = self.calculate_frequencies(self.playingnotes)
        self.voices = self.calculate_voices(frequencies, self.voices)
        samples_list = [voice.play() for voice in self.voices]
        # samples = self.sum_samples_temp(samples_list)
        samples = self.sum_samples(samples_list)
        return samples

    def register_notes_temporary(self, notes: list):
        self.pressednotes = notes
        self.release_times_temporary()

    def mode_select(self):
        self.playingnotes.sort()
        if self.mode == "mono":
            if len(self.playingnotes) > 0:
                notes = [self.playingnotes.pop()]
            else:
                notes = []
        return notes

    def release_times_temporary(self):
        self.playingnotes = self.pressednotes

    def calculate_frequencies(self, notes):
        frequencies = calculate_frequencies(notes)

        if self.mode == "mono":
            if len(frequencies) > 0:
                frequencies = [frequencies.pop()]
        elif self.mode == "poly":
            pass
        return frequencies

    def calculate_voices(self, frequencies, voices_old):
        voices = voices_old
        for frequency in frequencies:
            found = False
            for voice in voices:
                if voice.freq == frequency:
                    found = True
            if not found:
                voices.append(
                    Voice(frequency, self.oscillator_select, self.buffersize, self.samplerate))

        for voice in voices:
            if voice.freq not in frequencies:
                voices.remove(voice)

        return voices

    def sum_samples(self, samples_list):
        blank = np.asarray([0.0*256])
        samples_list.append(blank)
        samples = sum(samples_list)
        samples *= self.volume
        return samples
