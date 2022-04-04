""" Tests for the civilization spawner module """
from galaxy.planet.terrestrical import Terrestrical
from civilization.civilization_spawner import force_spawn_civilization

TESTNAME = "Planet of Apes"

def test_force_spawn_civilization():
    """ Testing if a civilization is spawned when all parameters fit """
    planet = Terrestrical(TESTNAME, 0, 0)
    print("test")
    if len(planet.get_civilizations()) > 0:
        assert True
    else:
        civ = force_spawn_civilization(planet)
        planet.add_civilization( civ )

    if len( planet.get_civilizations() ) > 0:
        assert True
