"""This module defines objects in regards to pysical properties and locations"""
from object.position import Position

class Object(Position):
    """This class defines objects in regards to pysical properties and locations"""
    def __init__(self, name):
        super().__init__(0,0)
        self.name = name
        print(self.name)

    def get_name(self):
        """This method returns the name of the object"""
        return self.name
