""" Tests for the belief module """
from civilization.belief.belief import Belief

def test_get_name():
    """ Testing the get name functionality """
    belief_name = "Pastafarianism"
    belief = Belief(belief_name, 0.5)
    assert belief.get_name() == belief_name
