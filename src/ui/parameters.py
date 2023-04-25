class Parameters:
    def __init__(self):
        self.vol = 127
        self.osc = 2
        self.polyphony = "poly"
        self.volume = 1
    
    def get_osc(self):
        return self.osc

    def set_osc(self, mode):
        if mode == "saw":
            self.osc = 2
        if mode == "square":
            self.osc = 1
    
    def get_volume(self):
        return self.volume

    def set_volume(self, vol):
        self.volume = vol
    
    def get_polyphony(self):
        return self.polyphony

    def set_polyphony(self, polyphony):
        self.polyphony = polyphony
