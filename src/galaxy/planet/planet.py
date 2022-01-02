"""This module defines planets"""
from random import gauss, randint, random
from object.object import Object
from civilization.civilization import Civilization

class Planet(Object):
    """This class defines planets"""
    def __init__(self, name):
        super().__init__(name)
        self.diameter = -1
        while self.diameter <= 0:
            self.diameter = int(gauss(12741000, 10000))
        self.min_temp = randint(-100, 100)
        self.max_temp = -100
        while self.min_temp < self.max_temp:
            self.max_temp = randint(-100, 100)
        self.atmosphere = random()
        self.hospitability = random()
        self.civilization_list = []
        self.civilization_list.append(Civilization("Humies"))

    def get_civilizations(self):
        """This method returns a list of civilizations living on this planet"""
        return self.civilization_list

    def get_size(self):
        """This method returns the size ( diameter ) in meters"""
        return self.diameter

    def step(self):
        """This method defines the behavour of this planet per step"""
        print("Step executed")
