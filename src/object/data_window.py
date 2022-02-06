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
        super().__init__(self.name, posx, posy)

    def step(self):
        """This MEthod defines the step behaviour of the Dataslate"""
        print("test")
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(str(self.name), True, config.WHITE)
        self.image.blit(text, (0,0))
