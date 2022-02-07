"""This module defines datawindows"""
import pygame
from object.object import Object
import config

class Dataslate(Object):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy):
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = 100
        self.height = 100
        self.parent = None
        super().__init__(self.name, posx, posy)

    def step(self):
        """This Method defines the step behaviour of the Dataslate"""
        font = pygame.font.SysFont('Arial', 20)
        writetext = self.parent.get_dataslate_data()
        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (0,0))

    def set_parent(self, parent):
        """This method sets the parent class of this dataslate"""
        self.parent = parent
