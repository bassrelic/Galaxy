""" Tests for the belief module """
from civilization.belief.belief import Belief

def test_get_name():
    """ Testing the get name functionality """
    belief_name = "Pastafarianism"
    belief = Belief(belief_name, 0.5)
    assert belief.get_name() == belief_name
    assert belief.get_intensity() == 0.5

def test_gen_belief():
    """ Testing the generate random functionality """
    belief = Belief.gen_random_belief()
    assert belief.get_name() == "standard"
    assert belief.get_intensity() > 0
    assert belief.get_intensity() < 1
