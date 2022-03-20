""" Tests for the Planet Module """
import pygame
import config
from galaxy.planet.planet import Planet


def test_baseclass_not_instanciable():
    """ Planet is a baseclass and should never be instantiated itself. Path (Image of graphic) must be supplied. """
    name = "HolyTerra"
    try:
        # pylint: disable-next=unused-variable; expected because this should throw an exception
        planet = Planet(name, 1, 2)
        assert False
    except AttributeError:
        assert True
