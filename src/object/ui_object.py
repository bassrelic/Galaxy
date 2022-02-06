"""This module implements positional information"""
import pygame
WHITE = (255, 255, 255)
class UiObject(pygame.sprite.Sprite):
    """This class implements positional information"""
    def __init__(self, posx, posy):
        # Call the parent class (Sprite) constructor
        super().__init__()

        if self.path is not None:
            # Pass in the color of the car, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)

            # Instead we could load a proper pciture of a car...
            self.image = pygame.transform.scale( pygame.image.load(self.path).convert_alpha(),
                                                    (self.width, self.height))

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
            self.rect.x = posx
            self.rect.y = posy
            print(f'Position: ({self.rect.x}, {self.rect.y})')

    def getx_pos(self):
        """This method gets the x position"""
        return self.rect.x

    def gety_pos(self):
        """This method gets the y position"""
        return self.rect.y

    def setx_pos(self, posx):
        """This method sets the x position"""
        self.rect.x = posx

    def sety_pos(self, posy):
        """This method sets the y position"""
        self.rect.y = posy
