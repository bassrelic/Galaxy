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
        self.width = 200
        self.height = 150
        self.set_path()
        self.parent = None

    def step(self):
        """This Method defines the step behaviour of the Dataslate"""
        font = pygame.font.SysFont('Arial', 16)
        self.set_path()
        writetext = ''
        y_pos_text = 20

        writetext = "testtext"
        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (15, y_pos_text))
        y_pos_text = y_pos_text + 15
