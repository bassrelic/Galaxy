"""This module defined a civilization"""
from random import random
from civilization.language.language import Language
from civilization.belief.belief import Belief
from technology.technology import Technology

class Civilization:
    """This class shall define a civilization"""
    def __init__(self, name):
        self.name = name
        self.language = Language("English")
        self.count = int(random()*100000)
        self.technologie_list = []
        self.belief_list = []
        self.technologie_list.append(Technology("Fire"))
        self.belief_list.append(Belief("God", 0.5))
        self.belief_list.append(Belief.gen_random_belief())

    def get_name(self):
        """This method returns the name of this civilization"""
        return self.name

    def get_beliefs(self):
        """This method returns a list of beliefs this civilization has"""
        return self.belief_list

    def get_count(self):
        """This Method returns the count of individuals this civilization consists of"""
        return self.count
