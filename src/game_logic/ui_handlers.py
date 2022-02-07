"""This module defines defines how the dataslate is being handeled"""
import pygame
from object.data_window import Dataslate

class DataslateHandler():
    """This class defines how the dataslate is being handeled"""
    def __init__(self):
        self.selected_sprite = None
        self.dataslate = None

    def handle_dataslate(self, all_sprites_list):
        """ This Method handles the dataslate manipulation """

        # Check cursor position
        mouse_position = pygame.mouse.get_pos()

        for sprite in all_sprites_list:
            # pylint: disable-next=no-else-break
            if sprite.rect.collidepoint(mouse_position):
                self.selected_sprite = sprite
                break
            else:
                self.selected_sprite = None

        if self.selected_sprite is not None:
            print("clicked object: " + self.selected_sprite.get_name())
            mouse_x_pos = pygame.mouse.get_pos()[0]
            mouse_y_pos = pygame.mouse.get_pos()[1]
            intermed_obj = Dataslate(self.selected_sprite.get_name(), mouse_x_pos, mouse_y_pos)

            if self.dataslate is not None:
                if intermed_obj.get_name() is not self.dataslate.get_name():
                    all_sprites_list.remove(self.dataslate)
                    del self.dataslate
                    self.dataslate = Dataslate(self.selected_sprite.get_name(), mouse_x_pos, mouse_y_pos)
                    all_sprites_list.add(self.dataslate)
                    self.dataslate.set_parent(self.selected_sprite)
                else:
                    all_sprites_list.remove(self.dataslate)
                    del self.dataslate
                    self.dataslate = None
                    print("triggered delete")
            else:
                self.dataslate = Dataslate(self.selected_sprite.get_name(), mouse_x_pos, mouse_y_pos)
                all_sprites_list.add(self.dataslate)
                self.dataslate.set_parent(self.selected_sprite)

            del intermed_obj
