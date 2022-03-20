""" Tests for the Planet Module """
import pygame
import config
from galaxy.planet.astroid import Astroid

config.screen = pygame.display.set_mode((500, 500))

def test_astroid_get_naem():
    """ Test instantiation and naming of astroid. """
    astroid = Astroid("99942 Apophis", 0, 1)
    assert astroid.get_name() == "99942 Apophis"
