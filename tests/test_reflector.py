from string import ascii_uppercase

import pytest

from enigma.enigma_machine import Reflector


@pytest.fixture
def reflector_A_wiring():
    return [ascii_uppercase.index(char) for char in "EJMZALYXVBWFCRQUONTSPIKHGD"]


@pytest.fixture
def reflector_A(reflector_A_wiring):
    return Reflector(wiring=reflector_A_wiring)


def test_reflector_has_wiring(reflector_A, reflector_A_wiring):
    assert reflector_A.wiring == reflector_A_wiring


@pytest.mark.parametrize(
    "input,output",
    (
        (0, 4),
        (4, 0),
        (1, 9),
        (9, 1),
        (25, 3),
        (3, 25),
    ),
)
def test_reflector_A_connection(reflector_A, input, output):
    assert reflector_A.connection(input) == output


def test_wiring_string():
    reflector = Reflector(wiring=list(range(26)))
    assert reflector.wiring_string() == ascii_uppercase


def test_repr():
    reflector = Reflector(wiring=list(range(26)))
    assert repr(reflector) == "<Reflector: ABCDEFGHIJKLMNOPQRSTUVWXYZ>"
