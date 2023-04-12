import pygame
from ui.keypresses import Keyboardinput


class Ui:
    def __init__(self):
        self.keyboardinput = Keyboardinput()

    def read_keypresses(self, event):
        self.keyboardinput.read_keypresses(event)

    def get_notes(self):
        notes = self.keyboardinput.get_notes()
        return notes
