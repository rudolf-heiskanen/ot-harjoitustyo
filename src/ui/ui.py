import pygame

class Ui:
    def __init__(self):
        self.keypresses = []
        self.notes = []
    
    def read_keypresses_temporary(self, event):
        if event.type == pygame.KEYDOWN:
            self.keypresses.append("A")
        elif event.type == pygame.KEYUP:
            self.keypresses.pop()
    
    def get_notes(self):
        self.calculate_notes_temporary()
        return self.notes
    
    def calculate_notes_temporary(self):
        for press in self.keypresses:
            if press == "A":
                self.notes.append("c3")