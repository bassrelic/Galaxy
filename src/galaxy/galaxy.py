"""This module defines a galaxy"""
from galaxy.system.system import System

class Galaxy:
    """This class defines a galaxy"""
    def __init__(self, name):
        self.name = name
        self.sol_list = []
        self.sol_list.append(System("Sun"))
        self.sol_list.append(System("Saggritarius"))
        print(f'This Galaxy is called {self.name}')

    def get_sols(self):
        """This method gets a list of associated solarsystems"""
        return self.sol_list
