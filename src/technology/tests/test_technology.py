""" Tests for the technology module """
from technology.technology import Technology

def test_get_name():
    """ Test of the get_name method """
    name = "MicroMaxiFluxCapacitor"
    definition = {
        "description": "Test",
        "research": 999,
        "prereq":{
            "name": "Optics"
        }
    }
    technology = Technology(name, definition)
    assert technology.get_name() == name

def test_get_all_technology_list():
    """Test of the get_all_technology_list method by checking for some major keys"""
    data = Technology.get_all_technology_list()
    keylist = ["Laser", "Habitat", "Sensormodule"]
    found_keys = 0
    datalist = list(data.items())[0][1]
    for mayor_key in datalist:
        if mayor_key["name"] in keylist:
            found_keys = found_keys + 1

    assert found_keys == len(keylist)
