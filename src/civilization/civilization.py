"""This module defined a civilization"""
from civilization.language.language import Language
from civilization.belief.belief import Belief
from technology.technology import Technology

class Civilization:
    """This class shall define a civilization"""
    def __init__(self, name):
        self.name = name
        self.language = Language("English")
        self.technologie_list = []
        self.belief_list = []
        self.technologie_list.append(Technology("Fire"))
        self.belief_list.append(Belief("God", 0.5))
        self.belief_list.append(Belief.gen_random_belief())

    def get_name(self):
        return self.name

    def get_beliefs(self):
        return self.belief_list
