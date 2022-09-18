"""This module defines datawindows"""
import pygame
from object.object import Object
import config

class Console(Object):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = pygame.display.get_window_size()[0]
        self.height = 300
        self.set_path()
        self.parent = None
        self.consoleTextList = ["~~~This is the console, feel free to try stuff~~~"]

    def step(self):
        """This Method defines the step behaviour of the Dataslate"""
        font = pygame.font.SysFont('Arial', 20)
        self.set_path()
        titleText = self.name
        text = font.render(str(titleText), True, config.WHITE)
        self.image.blit(text, (75, 10))
        y_pos_text = 40

        for element in self.consoleTextList:
            writetext = element
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (125, y_pos_text))
            y_pos_text = y_pos_text + 25
#        for data_type, data_value in data_dict.items():
#            writetext = str(data_type) + " : " + str(data_value)
#            
#            self.image.blit(text, (100, y_pos_text))
#            y_pos_text = y_pos_text + 15
