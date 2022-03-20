""" Tests for the Planet Module """
import random
import pygame
import pytest
import config
from galaxy.planet.astroid import Astroid

config.screen = pygame.display.set_mode((500, 500))

def test_astroid_get_name():
    """ Test instantiation and naming of astroid. """
    astroid = Astroid("99942 Apophis", 0, 1)
    assert astroid.get_name() == "99942 Apophis"

def test_get_civilizations():
    """This method tests if the get method returns a list of civilizations living on this planet
    Not implemented in class right now, skipping"""

def test_get_size():
    """This method tests returns the size ( diameter ) in meters"""
    astroid = Astroid("99942 Apophis", 0, 1)
    assert float( astroid.get_size() ) >= 1.00

def test_get_min_temp():
    """This Method tests the minimum temperature in °C"""
    astroid = Astroid("99942 Apophis", 0, 1)
    assert astroid.get_min_temp() == -100

def test_get_max_temp():
    """This Method tests the maximal temperature in °C"""
    astroid = Astroid("99942 Apophis", 0, 1)
    assert astroid.get_max_temp() == -100

def test_set_temp_range():
    """This method lets tests the set of the temperature range on this planet
    For now, temperature is not checked in regards to max > min """
    astroid = Astroid("99942 Apophis", 0, 1)
    testruns = 0
    while testruns < 100:
        min_temp = random.randint( -1000, 1000 )
        max_temp = random.randint( -1000, 1000 )
        astroid.set_temp_range(min_temp, max_temp)
        assert astroid.get_min_temp() == min_temp
        assert astroid.get_max_temp() == max_temp
        testruns += 1

def test_set_atmosphere():
    """This method tests the atmosphere quality (between 0 and 1)"""
    astroid = Astroid("99942 Apophis", 0, 1)
    assert float( astroid.get_atmosphere() ) == 0
    astroid.set_atmosphere(0.5)
    assert float( astroid.get_atmosphere() ) == 0.50

def test_set_diameter():
    """This method tests the get diameter method"""
    astroid = Astroid("99942 Apophis", 0, 1)
    astroid.set_diameter(0.5)
    assert float( astroid.get_size() ) == 0.5

def test_set_hospitability():
    """This method tests the get hospitability method (between 0 and 1)"""
    astroid = Astroid("99942 Apophis", 0, 1)
    assert float( astroid.get_hospitability() ) == 0.0
    astroid.set_hospitability( float(0.5) )
    assert float( astroid.get_hospitability() ) == 0.5

   # Test if ValueError is thrown correctly
    with pytest.raises(ValueError):
        astroid.set_hospitability(2)

def test_get_dataslate_data():
    """This method tests the returned dict containing the necessairy data for the corresponding dataslate"""
    astroid = Astroid("99942 Apophis", 0, 1)

    astroid.set_diameter(2000)
    astroid.set_atmosphere(0.5)
    astroid.set_hospitability(0.6)
    data = astroid.get_dataslate_data()

    assert data["Name"] == "99942 Apophis"
    assert data["min temp"] == "-100 °C"
    assert data["max temp"] == "-100 °C"
    assert data["diameter"] == "2000.00 km"
    assert data["atmosphere"] == "0.50 %"
    assert data["hospitability"] == "0.60 %"
