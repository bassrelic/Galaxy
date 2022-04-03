"""This module defines Astroids"""
from random import random, gauss, randint
from galaxy.planet.planet import Planet
from civilization.civilization_spawner import spawn_civilization

class Terrestrical(Planet):
    """This class defines a terrestrical Planet"""
    def __init__(self, name, posx, posy):
        self.path = "res\\planets\\gas\\gasPlanet_0.png"
        self.width = 100
        self.height = 100
        super().__init__(name, posx, posy)
        diameter = -1
        while diameter <= 0:
            diameter = int(gauss(12741000, 10000))
        self.set_diameter(diameter)
        min_temp = randint(-100, 100)
        max_temp = -100
        while min_temp > max_temp:
            max_temp = randint(-100, 100)
        self.set_temp_range(min_temp, max_temp)
        self.set_atmosphere(random())
        self.set_hospitability(random())

        new_civ = spawn_civilization(self)
        if new_civ is not None:
            self.civilization_list.append( new_civ )
