""" Tests for the Planet Module """
import random
import pygame
import pytest
from civilization.civilization import Civilization
import config
from galaxy.planet.terrestrical import Terrestrical

config.screen = pygame.display.set_mode((500, 500))

def test_terrestrical_get_name():
    """ Test instantiation and naming of terrestrical. """
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    assert terrestrical.get_name() == "99942 Apophis"

def test_get_civilizations():
    """This method tests if the get method returns a list of civilizations living on this planet
    Not implemented in class right now, skipping"""

def test_get_size():
    """This method tests returns the size ( diameter ) in meters"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    assert float( terrestrical.get_size() ) >= 1.00

def test_set_temp_range():
    """This method lets tests the set of the temperature range on this planet
    For now, temperature is not checked in regards to max > min """
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    testruns = 0
    while testruns < 100:
        min_temp = random.randint( -1000, 1000 )
        max_temp = random.randint( -1000, 1000 )
        terrestrical.set_temp_range(min_temp, max_temp)
        assert terrestrical.get_min_temp() == min_temp
        assert terrestrical.get_max_temp() == max_temp
        testruns += 1

def test_set_atmosphere():
    """This method tests the atmosphere quality (between 0 and 1)"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    terrestrical.set_atmosphere(0.5)
    assert float( terrestrical.get_atmosphere() ) == 0.50

def test_set_diameter():
    """This method tests the get diameter method"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    terrestrical.set_diameter(0.5)
    assert float( terrestrical.get_size() ) == 0.5

def test_set_hospitability():
    """This method tests the get hospitability method (between 0 and 1)"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    terrestrical.set_hospitability( float(0.5) )
    assert float( terrestrical.get_hospitability() ) == 0.5

   # Test if ValueError is thrown correctly
    with pytest.raises(ValueError):
        terrestrical.set_hospitability(2)

def add_civilization():
    """This method tests the add civilization method"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)
    civ = Civilization("Marsians")
    terrestrical.add_civilization(civ)

    civ_list = terrestrical.get_civilizations()
    assert len(civ_list) == 1
    assert civ_list[1].get_name() == "Marsians"

def test_get_dataslate_data():
    """This method tests the returned dict containing the necessairy data for the corresponding dataslate"""
    terrestrical = Terrestrical("99942 Apophis", 0, 1)

    terrestrical.set_temp_range(-100, 100)
    terrestrical.set_diameter(2000)
    terrestrical.set_atmosphere(0.5)
    terrestrical.set_hospitability(0.6)
    civ = Civilization("Marsians")
    terrestrical.add_civilization(civ)

    data = terrestrical.get_dataslate_data()

    assert data["Name"] == "99942 Apophis"
    assert data["min temp"] == "-100 °C"
    assert data["max temp"] == "100 °C"
    assert data["diameter"] == "2000.00 km"
    assert data["atmosphere"] == "0.50 %"
    assert data["hospitability"] == "0.60 %"
    assert data["civilizations"] == "Marsians"
