"""This module defines datawindows"""
from object.ui_object import UiObject

class Dataslate(UiObject):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy):
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = 100
        self.height = 100
        super().__init__(posx, posy)
        print(self.name)


    def get_name(self):
        """This method returns the name of the object"""
        return self.name

    def set_graphic_path(self, path):
        """This method lets you set the path to the applicable graphic"""
        self.path = path
