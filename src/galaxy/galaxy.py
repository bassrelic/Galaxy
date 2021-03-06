"""This module defines a galaxy"""
from galaxy.system.system import System

class Galaxy:
    """This class defines a galaxy"""
    def __init__(self, name):
        self.name = name
        self.sol_list = []
        self.sol_list.append(System("Sun"))
        print(f'This Galaxy is called {self.name}')

    def get_sols(self):
        """This method gets a list of associated solarsystems"""
        return self.sol_list

    def step(self):
        """This method defines the behavour of this galaxy per step"""
