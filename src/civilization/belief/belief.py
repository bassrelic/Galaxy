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
        with open('src\\civilization\\belief\\beliefs.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            #for mayor_key in data.items():
                #print(mayor_key)
        name = "standard"
        intensity = random()
        return Belief(name, intensity)

    def get_name(self):
        """This method returns the name of this belief"""
        return self.name

    def get_intensity(self):
        """This method returns the intensity of this belief"""
        return self.intensity
