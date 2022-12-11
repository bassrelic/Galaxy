"""This module defines the research window"""
import json
import pygame
from object.object import Object
from object.tech_window import Tech
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
        self.technologie_list = []
        self.tech_object_list = []
        self.__get_all_technology_list()
        self.__setup()

    def step(self):
        """This Method defines the step behaviour of the Research window"""
        font_size_header = 32
        font = pygame.font.SysFont('Arial', font_size_header)
        self.set_path()

        writetext = "Research"
        x_pos_text = self.width / 2 + self.posx - ( len(writetext) * font_size_header ) / 2
        y_pos_text = self.posy + 50

        text = font.render(str(writetext), True, config.WHITE)
        self.image.blit(text, (x_pos_text, y_pos_text))

        for item in self.tech_object_list:
            item.step()

    @staticmethod
    def get_dataslate_data():
        """This object does not have dataslate Date to show."""
        return None

    def get_sprites(self):
        """This method returns all children sprites (techs)"""
        return self.tech_object_list

    def __setup(self):
        """This method is used to setup the research window."""
        x_pos = self.posx + 130
        y_pos = self.posy + 100
        for tech in self.technologie_list:
            techwindow = Tech(tech.get_name(), x_pos, y_pos, tech)
            self.tech_object_list.append(techwindow)
            y_pos = y_pos + 40


    def __get_all_technology_list(self):
        """This method generates a List containing all technologies"""
        with open('src\\technology\\technologies.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            techs = data["technologies"]
            for tech in techs:
                self.technologie_list.append(Technology( tech["name"], tech ))
