from civilization.belief.belief import Belief

def test_get_name():
    beliefName = "Pastafarianism"
    belief = Belief(beliefName, 0.5)
    assert belief.get_name() == beliefName
