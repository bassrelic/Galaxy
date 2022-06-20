"""This module defined a civilization"""
from random import randint, random
from civilization.language.language import Language
from civilization.belief.belief import Belief
from technology.technology import Technology

class Civilization:
    """This class shall define a civilization"""
    def __init__(self, name):
        self.name = name
        self.language = Language("English")
        self.count = int(random()*1000000)
        self.technologie_list = []
        self.belief_list = []
        self.belief_list.append(Belief("God", 0.5))
        self.belief_list.append(Belief.gen_random_belief())
        self.min_atmosphere = random()
        self.min_temp = randint(-100, 100)
        self.max_temp = -1000
        self.reproduction_rate_pa = 1.05
        self.stepcounter = 0
        while self.max_temp < self.min_temp:
            self.max_temp = randint(-100, 100)

    def get_name(self):
        """This method returns the name of this civilization"""
        return self.name

    def get_beliefs(self):
        """This method returns a list of beliefs this civilization has"""
        return self.belief_list

    def get_technologies(self):
        """This method returns a list of technologies this civilization has"""
        return self.technologie_list

    def get_count(self):
        """This Method returns the count of individuals this civilization consists of"""
        return self.count

    def get_min_atmosphere(self):
        """This Method returns the minimal atmosphere value a planet must provide in order to be hospitable for this
        civilization"""
        return self.min_atmosphere

    def get_min_temp(self):
        """This Method returns the minimal temperature value a planet must provide in order to be hospitable for this
        civilization"""
        return self.min_temp

    def get_max_temp(self):
        """This Method returns the maximal temperature value a planet must provide in order to be hospitable for this
        civilization"""
        return self.max_temp

    def get_reproduction_rate(self):
        """This method returns the reproduction rate"""
        return self.reproduction_rate_pa

    def set_reproduction_rate(self, reproduction_rate):
        """This method sets the reproduction rate"""
        self.reproduction_rate_pa = reproduction_rate

    def step(self):
        """This method defines the behavour of this civilization per step"""
        self.stepcounter = self.stepcounter + 1
        if self.stepcounter == 60:
            self.stepcounter = 0
            self.__reproduce_daily()

    def __reproduce_daily(self):
        """This method reproduces the civilization"""
        reproduction_per_day = ((self.reproduction_rate_pa - 1) / 365 ) + 1
        self.count = self.count * reproduction_per_day
