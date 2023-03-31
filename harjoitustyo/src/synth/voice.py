from synth.oscillators import Oscillator

class Voice:
    def __init__(self, freq, wave, buffersize, samplerate, filtersettings = False, filter_adsr = False, amp_adsr = False):
        self.freq = freq
        self.wave = wave
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.filtersettings = filtersettings
        self.filter_adsr = filter_adsr
        self.amp_adsr = amp_adsr

        self.oscillator = Oscillator(self.freq, self.wave, self.buffersize, self.samplerate)
        
    def play(self):
        raw_wave = self.oscillator.oscillate()
        
        return raw_wave
