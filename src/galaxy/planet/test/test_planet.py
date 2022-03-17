""" Tests for the Planet Module """
import pygame
import config
from galaxy.planet.planet import Planet
from galaxy.planet.astroid import Astroid

config.screen = pygame.display.set_mode((500, 500))

def test_baseclass_not_instanciable():
    """ Planet is a baseclass and should never be instantiated itself. Path (Image of graphic) must be supplied. """
    name = "HolyTerra"
    try:
        # pylint: disable-next=unused-variable; expected because this should throw an exception
        planet = Planet(name, 1, 2)
        assert False
    except AttributeError:
        assert True

def test_astroid_get_naem():
    """ Test instantiation and naming of astroid. """
    astroid = Astroid("99942 Apophis", 0, 1)
    assert astroid.get_name() == "99942 Apophis"
