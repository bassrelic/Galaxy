from civilization.civilization import Civilization

def test_get_name():
    testname = "testerarier"
    civ =Civilization(testname)
    assert civ.get_name() == testname