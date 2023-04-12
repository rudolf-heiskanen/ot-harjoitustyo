from synth.oscillators import Oscillator


class Voice:
    def __init__(self, freq, wave, buffersize,
    samplerate, filtersettings=False, adsr=(False, False)):
        self.freq = freq
        self.wave = wave
        self.buffersize = buffersize
        self.samplerate = samplerate
        self.filtersettings = filtersettings
        self.amp_adsr = adsr[0]
        self.filter_adsr = adsr[1]

        self.oscillator = Oscillator(
            self.freq, self.wave, self.buffersize, self.samplerate)

    def play(self):
        raw_wave = self.oscillator.oscillate()

        return raw_wave
