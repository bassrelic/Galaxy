"""This method implements positional information"""
class Position:
    """This class implements positional information"""
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        print(f'Position: ({self.posx}, {self.posy})')

    def getx_pos(self):
        """This method gets the x position"""
        return self.posx

    def gety_pos(self):
        """This method gets the y position"""
        return self.posy

    def setx_pos(self, posx):
        """This method sets the x position"""
        self.posx = posx

    def sety_pos(self, posy):
        """This method sets the y position"""
        self.posy = posy
