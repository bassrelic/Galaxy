""" Tests for the civilization module """
from civilization.civilization import Civilization
from civilization.belief.belief import Belief
from technology.technology import Technology


TESTNAME = "testerarier"
civ =Civilization(TESTNAME)

def test_get_name():
    """ Testing the get_name method """
    assert civ.get_name() == TESTNAME

def test_get_count():
    """ Testing the get_count method """
    assert civ.get_count() >= 0

def test_get_beliefs():
    """ Testing the get_beliefs method and objtype """
    beliefs = civ.get_beliefs()
    assert beliefs[0].get_name() == "God"
    for obj in beliefs:
        assert isinstance(obj, Belief)

def test_get_technologies():
    """ Testing the get_technologies method and objtype """
    technologies = civ.get_technologies()
    assert technologies[0].get_name() == "Fire"
    for obj in technologies:
        assert isinstance(obj, Technology)

def test_get_min_atmosphere():
    """ Testing the get_min_atmosphere method"""
    atmosphere = civ.get_min_atmosphere()
    assert atmosphere >= 0
    assert atmosphere <= 1

def test_get_min_temp():
    """ Testing the get_min_temp method"""
    temp = civ.get_min_temp()
    assert temp <= 100
    assert temp >= -100

def test_get_max_temp():
    """ Testing the get_max_temp method"""
    temp = civ.get_max_temp()
    assert temp <= 100
    assert temp >= -100

def test_temp_range():
    """ Testing if min temp < max temp"""
    min_temp = civ.get_min_temp()
    max_temp = civ.get_max_temp()

    assert min_temp <= max_temp
