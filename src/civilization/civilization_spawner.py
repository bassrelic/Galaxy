"""This module defined a spawner checking environment values to spawn a civilization"""
from civilization.civilization import Civilization

def spawn_civilization(planet):
    """This Funciton checks if the given civilization can exist and thus spawn on the given planet"""
    civ = Civilization("test")
    civ_min_temp = civ.get_min_temp()
    civ_max_temp = civ.get_max_temp()
    civ_min_atmosphere = civ.get_min_atmosphere()
    print( "Civ: " + str(civ_min_temp) + " " + str(civ_max_temp) + " " + str(civ_min_atmosphere) )

    pl_min_temp = planet.get_min_temp()
    pl_max_temp = planet.get_max_temp()
    pl_atmosphere = planet.get_atmosphere()
    print( "Planet:" + str(pl_min_temp) + " " + str(pl_max_temp) + " " + str(pl_atmosphere) )

    if (
         civ.get_min_temp() <= planet.get_min_temp() and
         civ.get_max_temp() >= planet.get_max_temp() and
         civ.get_min_atmosphere() <= float(planet.get_atmosphere())
        ):
        print("SPAWNER:   Spawning civ")
        return civ

    print("SPAWNER:   Nothing Spawned")
    return None
