"""This module defines a language"""

from random import random

class Language:
    """This class shall define a language"""
    def __init__(self, name):
        self.name = name
        self.complexity = random()

    def get_name(self):
        """This method returns the name of this language"""
        return self.name

    def get_complexity(self):
        """This method returns the complexity of this language"""
        return self.complexity
