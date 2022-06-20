"""This module defines the research window"""
import pygame
import json
from object.object import Object
from technology.technology import Technology
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
        self.technologielist = []
        self.__get_all_technology_list()

    def step(self):
        """This Method defines the step behaviour of the Research window"""
        font_size_header = 32
        font_size_lines = 24
        font = pygame.font.SysFont('Arial', font_size_header)
        self.set_path()

        writetext = "Research"
        x_pos_text = self.width / 2 + self.posx - ( len(writetext) * font_size_header ) / 2
        y_pos_text = self.posy + 50

        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos_text, y_pos_text))

        x_pos_text = self.posx + 130
        y_pos_text = self.posy + 100
        font = pygame.font.SysFont('Arial', font_size_lines)
        for tech in self.technologielist:
            writetext = tech.get_name()
            y_pos_text = y_pos_text + 40
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (x_pos_text, y_pos_text))
            x_pos = x_pos_text + 500
            writetext = tech.get_research()
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (x_pos, y_pos_text))
            x_pos = x_pos + 75
            writetext = tech.get_description()
            text = font.render(str(writetext), True, config.WHITE)
            self.image.blit(text, (x_pos, y_pos_text))

    def __get_all_technology_list(self):
        """This method generates a List containing all technologies"""
        with open('src\\technology\\technologies.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            techs = data["technologies"]
            for tech in techs:
                self.technologielist.append(Technology( tech["name"], tech ))
