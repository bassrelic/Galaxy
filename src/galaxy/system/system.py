"""This module defines a System"""
from galaxy.planet.planet import Planet
from object.object import Object

class System(Object):
    """This class defines a System"""
    def __init__(self, name):
        super().__init__(name)
        self.planet_list = []
        self.planet_list.append(Planet("Earth"))

    def get_planets(self):
        """This method gets the list of associated planets"""
        return self.planet_list
