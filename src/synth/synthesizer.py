from time import time
from synth.synthengine import Synthengine
from synth.playback import Playbackdevice
from ui.ui import Ui


class Synthesizer:
    """Luokka, joka vastaa ohjelman pääloopin pyörittämisestä

    Luokka hoitaa myös informaation välittämisen käyttöliittymän ja sovelluslogiikan välillä.
    
    Attributes:
        buffersize: Kuinka monta samplea (yksittäinen äänenvoimakkuutta kuvaava lukuarvo joista
          digitaalinen audio koostuu) ohjelma laskee ennen kuin se lähettää
          lasketut samplet äänentoistosta vastaavalle osalle
        samplerate: Kuinka moneen sampleen yksi sekunti on jaettu
        duration: Bufferin koko sekunteina
        last: Viimeinen ajan hetki, kun samplet on lähetetty äänentoistosta
          vastaavalle osalle
        clock: Tämänhetkinen ajan hetki
        synthengine: Ohjelman luokka, joka johtaa nuottidatan muuttamista lopulta audioksi,
          joka voidaan lähettää äänentoistolle
        playback: Ohjelman luokka, joka vastaa äänen toistamisesta kaiuttimista
        ui: Käyttöliittymästä vastaava luokka
    """

    def __init__(self):
        """Luokan konstruktori, joka vastaa kaikkien edellä mainittujen attribuuttien alustamisesta.
        """
        self.buffersize = 2048
        self.samplerate = 44100

        self.duration = self.buffersize / self.samplerate / 1.0
        self.last = 0
        self.clock = 0

        self.synthengine = Synthengine(self.buffersize, self.samplerate)
        self.playbackdevice = Playbackdevice(self.buffersize, self.samplerate)
        self.ui = Ui()

    def run(self):
        """Ohjelman pääloopin pyörittämisestä vastaava metodi
        
        Vastaa pääloopin pyörittämisestä ja sen tarvittaessa keskeyttämisestä.
        Kutsutaan ohjelman käynnistyksen yhteydessä. Vastaa kellon ylläpitämisestä.
        Informaation välitys käyttöliittymän ja sovelluslogiikan välillä tapahtuu
        loopin sisällä.
        """
        
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
            self.synthengine.register_notes(notes)

            # timed events

            if self.clock - self.last > self.duration:
                self.playbackdevice.play(samples)
                self.last = self.clock
                self.ui.timed_events()
                samples = self.synthengine.play_notes()
