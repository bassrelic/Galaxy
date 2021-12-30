"""This module defines a belief"""

from random import random
import json

class Belief:
    """This class shall define a belief"""
    def __init__(self, name, intensity):
        self.name = name
        self.intensity = intensity

    @classmethod
    def gen_random_belief(cls):
        """This method generates a random beief with random intensity"""
        with open('src\\civilization\\belief\\beliefs.json') as json_file:
            data = json.load(json_file)
            for mayorKey, subdict in data.items():
                print(mayorKey)
        name = "standard"
        intensity = random()
        return Belief(name, intensity)

    def get_name(self):
        return self.name
