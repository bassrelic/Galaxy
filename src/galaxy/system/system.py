"""This module defines a System"""
from galaxy.planet.terrestrical import Terrestrical
from galaxy.planet.astroid import Astroid
from galaxy.planet.star import Star
from object.object import Object

class System(Object):
    """This class defines a System"""
    def __init__(self, name):
        self.path = "res\\ui_elements\\empty.png"
        self.width = 0
        self.height = 0
        super().__init__(name, 0, 0)
        self.planet_list = []
        posx = 100
        posy = 200
        self.planet_list.append(Terrestrical("Earth", posx, posy))
        self.planet_list.append(Star("Sun", 200, 400))
        self.astroid_list = []
        astroid_name = str(self.name) + str("-Alpha-1")
        self.astroid_list.append(Astroid(astroid_name, 10, 15))

    def get_planets(self):
        """This method gets the list of associated planets"""
        return self.planet_list

    def get_astroids(self):
        """This method gets the list of associated astroids"""
        return self.astroid_list

    def get_dataslate_data(self):
        """This function returns a dict containing the necessairy data for the corresponding dataslate"""
        dataslate_data = {
            "Name:"          : self.name
        }

        return dataslate_data

    def step(self):
        """This method defines the behavour of this system per step"""
