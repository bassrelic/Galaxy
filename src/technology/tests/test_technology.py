""" Tests for the technology module """
from technology.technology import Technology

def test_get_name():
    """ Test of the get_name method """
    name = "MicroMaxiFluxCapacitor"
    technology = Technology(name)
    assert technology.get_name() == name
