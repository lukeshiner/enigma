from string import ascii_uppercase

import pytest

from enigma.enigma_machine import Reflector, Rotor


@pytest.fixture
def rotor_I_string():
    return "EKMFLGDQVZNTOWYHXUSPAIBRCJ"


@pytest.fixture
def rotor_I_wiring(rotor_I_string):
    return [ascii_uppercase.index(char) for char in rotor_I_string]


@pytest.fixture
def rotor_I_notches():
    return (17,)


@pytest.fixture
def rotor_I(rotor_I_wiring, rotor_I_notches):
    return Rotor(wiring=rotor_I_wiring, notches=rotor_I_notches)


@pytest.fixture
def rotor_II():
    wiring = [ascii_uppercase.index(char) for char in "AJDKSIRUXBLHWTMCQGZNPYFVOE"]
    notches = (ascii_uppercase.index("F"),)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_III():
    wiring = [ascii_uppercase.index(char) for char in "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
    notches = (ascii_uppercase.index("W"),)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_IV():
    wiring = [ascii_uppercase.index(char) for char in "ESOVPZJAYQUIRHXLNFTGKDCMWB"]
    notches = (ascii_uppercase.index("K"),)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_V():
    wiring = [ascii_uppercase.index(char) for char in "VZBRGITYUPSDNHLXAWMJQOFECK"]
    notches = (ascii_uppercase.index("A"),)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_VI():
    wiring = [ascii_uppercase.index(char) for char in "JPGVOUMFYQBENHZRDKASXLICTW"]
    notches = (0,)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_VII():
    wiring = [ascii_uppercase.index(char) for char in "NZJHGRCXMYSWBOUFAIVLPEKQDT"]
    notches = (0, 13)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def rotor_VIII():
    wiring = [ascii_uppercase.index(char) for char in "FKQHTLXOCBJSPDZRAMEWNIUYGV"]
    notches = (0, 13)
    return Rotor(wiring=wiring, notches=notches)


@pytest.fixture
def reflector_A():
    wiring = [ascii_uppercase.index(char) for char in "EJMZALYXVBWFCRQUONTSPIKHGD"]
    return Reflector(wiring)


@pytest.fixture
def reflector_B():
    wiring = [ascii_uppercase.index(char) for char in "YRUHQSLDPXNGOKMIEBFZCWVJAT"]
    return Reflector(wiring)


@pytest.fixture
def reflector_C():
    wiring = [ascii_uppercase.index(char) for char in "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
    return Reflector(wiring)
