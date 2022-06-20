"""This module defines the research window"""
import pygame
from object.object import Object
import config

class Research(Object):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = 1900
        self.height = 1000
        self.set_path()
        self.parent = None

    def step(self):
        """This Method defines the step behaviour of the Research window"""
        font_size = 32
        font = pygame.font.SysFont('Arial', font_size)
        self.set_path()

        writetext = "Research"
        x_pos_text = self.width / 2 + self.posx - ( len(writetext) * font_size ) / 2
        y_pos_text = self.posy + 50

        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos_text, y_pos_text))
