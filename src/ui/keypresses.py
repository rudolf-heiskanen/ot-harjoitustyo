import pygame


class Keyboardinput:
    def __init__(self):
        self.keypresses = []
        self.notes = []

    def read_keypresses(self, event):
        key = ""
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key = "A"
            elif event.key == pygame.K_w:
                key = "W"
            elif event.key == pygame.K_s:
                key = "S"
            elif event.key == pygame.K_e:
                key = "E"
            elif event.key == pygame.K_d:
                key = "D"
            elif event.key == pygame.K_f:
                key = "F"
            elif event.key == pygame.K_t:
                key = "T"
            elif event.key == pygame.K_g:
                key = "G"
            elif event.key == pygame.K_y:
                key = "Y"
            elif event.key == pygame.K_h:
                key = "H"
            elif event.key == pygame.K_u:
                key = "U"
            elif event.key == pygame.K_j:
                key = "J"
            elif event.key == pygame.K_k:
                key = "K"
        if event.type == pygame.KEYDOWN:
            self.keypresses.append(key)
        elif event.type == pygame.KEYUP:
            self.keypresses.remove(key)

    def calculate_notes(self):
        temp_list = []

        for press in self.keypresses:
            if press == "A":
                temp_list.append("c3")
            elif press == "W":
                temp_list.append("c#3")
            elif press == "S":
                temp_list.append("d3")
            elif press == "E":
                temp_list.append("d#3")
            elif press == "D":
                temp_list.append("e3")
            elif press == "F":
                temp_list.append("f3")
            elif press == "T":
                temp_list.append("f#3")
            elif press == "G":
                temp_list.append("g3")
            elif press == "Y":
                temp_list.append("g#3")
            elif press == "H":
                temp_list.append("a3")
            elif press == "U":
                temp_list.append("a#3")
            elif press == "J":
                temp_list.append("b3")
            elif press == "K":
                temp_list.append("c4")
        self.notes = temp_list

    def get_notes(self):
        self.calculate_notes()
        return self.notes
