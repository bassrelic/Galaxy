"""This module defines Astroids"""
from random import random, gauss
from galaxy.planet.planet import Planet

class Astroid(Planet):
    """This class defines planets"""
    def __init__(self, name):
        super().__init__(name)
        diameter = -1
        while diameter <= 0:
            diameter = int(gauss(100,1000))
        self.diameter = diameter
        self.min_temp = -100
        self.max_temp = -100
        self.atmosphere = 0
        self.hospitability = 0
        self.civilization_list = []
