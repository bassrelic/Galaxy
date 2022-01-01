"""This module defines planets"""
from object.object import Object
from civilization.civilization import Civilization

class Planet(Object):
    """This class defines planets"""
    def __init__(self, name):
        super().__init__(name)
        self.size = 0
        self.min_temp = 0
        self.max_temp = 0
        self.civilization_list = []
        self.civilization_list.append(Civilization("Humies"))

    def get_civilizations(self):
        """This method returns a list of civilizations living on this planet"""
        return self.civilization_list
