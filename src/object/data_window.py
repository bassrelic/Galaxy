"""This module defines datawindows"""
from object.object import Object

class Dataslate(Object):
    """This class defines datawindows in terms of size and looks"""
    def __init__(self, name, posx, posy):
        self.name = name
        self.path = "res\\ui_elements\\dataslate.png"
        self.width = 100
        self.height = 100
        super().__init__(self.name, posx, posy)
