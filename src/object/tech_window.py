"""This module defines a tech shown in the research window"""
import pygame
from object.object import Object
import config

class Tech(Object):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy, data):
        super().__init__(name, posx, posy)
        self.name = name
        self.path = "res\\ui_elements\\empty.png"
        self.width = 1500
        self.height = 100
        self.set_path()
        self.data = data

    def step(self):
        """This Method defines the step behaviour of the Research window"""
        font_size_header = 32
        font_size_lines = 24
        font = pygame.font.SysFont('Arial', font_size_header)
        self.set_path()

        writetext = self.name
        x_pos_text = self.posx
        y_pos_text = self.posy

        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos_text, y_pos_text))

        x_pos_text = 0
        y_pos_text = 0
        font = pygame.font.SysFont('Arial', font_size_lines)

        writetext = self.data.get_name()
        y_pos_text = y_pos_text + 40
        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos_text, y_pos_text))
        x_pos = x_pos_text + 500
        writetext = self.data.get_research()
        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos, y_pos_text))
        x_pos = x_pos + 75
        writetext = self.data.get_description()
        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos, y_pos_text))

    @staticmethod
    def get_dataslate_data():
        """This object doqes not have dataslate Date to show."""
        return None
