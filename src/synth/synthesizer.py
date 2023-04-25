from time import time
from synth.synthengine import Synthengine
from synth.playback import Playbackdevice
from ui.ui import Ui


class Synthesizer:
    def __init__(self):
        self.buffersize = 2048
        self.samplerate = 44100

        self.duration = self.buffersize / self.samplerate / 1.0
        self.last = 0
        self.clock = 0

        self.synthengine = Synthengine(self.buffersize, self.samplerate)
        self.playbackdevice = Playbackdevice(self.buffersize, self.samplerate)
        self.ui = Ui()

    def run(self):
        running = True
        samples = self.synthengine.play_notes()

        # program's main loop
        # communicates information from ui to synthengine and keeps timing

        while running:
            # constantly happening events

            self.clock = time()
            self.ui.check_events()
            self.synthengine.set_parameters(self.ui.get_parameters())
            if self.ui.get_exit():
                running = False

            self.synthengine.set_time(self.clock)
            notes = self.ui.get_notes()
            self.synthengine.register_notes_temporary(notes)

            # timed events

            if self.clock - self.last >= self.duration:
                self.playbackdevice.play(samples)
                self.last = self.clock
                self.ui.timed_events()
                samples = self.synthengine.play_notes()
