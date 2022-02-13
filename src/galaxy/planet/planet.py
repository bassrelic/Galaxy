"""This module defines planets"""
from object.object import Object

class Planet(Object):
    """This class defines planets"""
    def __init__(self, name, posx, posy):
        super().__init__(name, posx, posy)
        self.civilization_list = []
        self.min_temp = 0
        self.max_temp = 0
        self.atmosphere = 0
        self.diameter = 0
        self.hospitability = 0

    def get_civilizations(self):
        """This method returns a list of civilizations living on this planet"""
        return self.civilization_list

    def get_size(self):
        """This method returns the size ( diameter ) in meters"""
        return self.diameter

    def step(self):
        """This method defines the behavour of this planet per step"""

    def set_temp_range(self, min_temp, max_temp):
        """This method lets you set the temperature range on this planet"""
        self.min_temp = min_temp
        self.max_temp = max_temp

    def set_atmosphere(self, atmosphere):
        """This method lets you set the atmosphere quality (between 0 and 1)"""
        if 0 <= atmosphere <= 1:
            self.atmosphere = format(atmosphere, '.2f')
        else:
            raise ValueError("Number not between 0 and 1")

    def set_diameter(self, diameter):
        """This function lets you set the diameter"""
        self.diameter = format(diameter, '.2f')

    def set_hospitability(self, hospitability):
        """This method lets you set the hospitability quality (between 0 and 1)"""
        if 0 <= hospitability <= 1:
            self.hospitability = format(hospitability, '.2f')
        else:
            raise ValueError("Number not between 0 and 1")

    def get_dataslate_data(self):
        """This function returns a dict containing the necessairy data for the corresponding dataslate"""
        dataslate_data = {
            "Name"          : self.name,
            "min temp"      : str(self.min_temp) + " °C",
            "max temp"      : str(self.max_temp) + " °C",
            "diameter"      : str(self.diameter) + " km",
            "atmosphere"    : str(self.atmosphere) + " %",
            "hospitability" : str(self.hospitability) + "%",
        }

        return dataslate_data
