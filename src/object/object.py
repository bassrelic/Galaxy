"""This module defines objects in regards to pysical properties and locations"""
from object.ui_object import UiObject

class Object(UiObject):
    """This class defines objects in regards to pysical properties and locations"""
    def __init__(self, name, posx, posy):
        super().__init__(posx, posy)
        self.name = name
        self.path = None
        print(self.name)

    def get_name(self):
        """This method returns the name of the object"""
        return self.name

    def set_graphic_path(self, path):
        """This method lets you set the path to the applicable graphic"""
        self.path = path
