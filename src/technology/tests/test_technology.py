""" Tests for the technology module """
from technology.technology import Technology

def test_get_name():
    """ Test of the get_name method """
    name = "MicroMaxiFluxCapacitor"
    technology = Technology(name)
    assert technology.get_name() == name

def test_get_all_technology_list():
    """Test of the get_all_technology_list method by checking for some major keys"""
    data = Technology.get_all_technology_list()
    keylist = ["laser", "habitat", "sensormodule"]
    found_keys = 0
    for mayor_key in data.items():
        if mayor_key[0] in keylist:
            found_keys = found_keys + 1

    assert found_keys == len(keylist)
