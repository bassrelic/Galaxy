"""This module defines a System"""
from galaxy.planet.planet import Planet
from galaxy.planet.astroid import Astroid
from object.object import Object

class System(Object):
    """This class defines a System"""
    def __init__(self, name):
        super().__init__(name)
        self.planet_list = []
        self.planet_list.append(Planet("Earth"))
        self.astroid_list = []
        astroid_name = str(self.name) + str("-Alpha-1")
        self.astroid_list.append(Astroid(astroid_name))

    def get_planets(self):
        """This method gets the list of associated planets"""
        return self.planet_list

    def get_astroids(self):
        """This method gets the list of associated astroids"""
        return self.astroid_list
