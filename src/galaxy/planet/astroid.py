"""This module defines Astroids"""
from random import gauss
from galaxy.planet.planet import Planet

class Astroid(Planet):
    """This class defines planets"""
    def __init__(self, name, posx, posy):
        self.width = 50
        self.height = 50
        self.path = "res\\planets\\astroids\\astroid1_base.png"
        super().__init__(name, posx, posy)
        diameter = -1
        while diameter <= 0:
            diameter = int(gauss(100,1000))
        self.set_diameter( diameter )
        self.set_temp_range(-100, -100)
        self.set_atmosphere(0)
        self.set_hospitability(0)
