""" Tests for the language module """
from civilization.language.language import Language

LANGUAGE = "Ewokese"
lang = Language(LANGUAGE)

def test_language_name():
    """ Testing the get name method """
    assert lang.get_name() == LANGUAGE


def test_language_complexity():
    """ Testing the get complexity method and range """
    assert 0 <= lang.get_complexity() <= 1
