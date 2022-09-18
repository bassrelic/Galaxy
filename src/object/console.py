"""This module defines the console"""
import pygame
from object.object import Object
import config

class Console(Object):
    """This class defines the console in terms of size and looks"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = pygame.display.get_window_size()[0]
        self.height = 300
        self.set_path()
        self.parent = None
        self.console_text_list = ["~~~This is the console, feel free to try stuff~~~","$"]

    def step(self):
        """This Method defines the step behaviour of the Console"""
        font = pygame.font.SysFont('Arial', 20)
        self.set_path()
        title_text = self.name
        text = font.render(str(title_text), True, config.WHITE)
        self.image.blit(text, (75, 10))
        y_pos_text = 40

        for element in self.console_text_list:
            writetext = element
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (125, y_pos_text))
            y_pos_text = y_pos_text + 25

    def write_to_console(self, text):
        """This method defines the write to console behaviour"""
        list_length = len(self.console_text_list)
        if list_length > 1:
            prev_text = self.console_text_list.pop(list_length-1)
            if prev_text.startswith('$'):
                if len(prev_text) >= 1 and text != "\n":
                    self.console_text_list.append(str(prev_text + text))
                else:
                    self.console_text_list.append(prev_text)
                    self.console_text_list.append('$')
        else:
            self.console_text_list.append(str("$" + text))
        self._check_max_length()

    def _check_max_length(self):
        """This method checks the length of console inputs and removes anything over limit"""
        if len(self.console_text_list) > 10:
            self.console_text_list.pop(1)
