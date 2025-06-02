from string import ascii_uppercase

import pytest

from enigma.enigma_machine import Rotor


@pytest.fixture
def rotor(rotor_I_wiring, rotor_I_notches):
    return Rotor(wiring=rotor_I_wiring, notches=rotor_I_notches, ring_position=0)


def test_rotor_has_wiring(rotor, rotor_I_wiring):
    assert rotor.wiring == rotor_I_wiring


def test_rotor_has_notches(rotor):
    assert rotor.notches == {17}


def test_rotor_has_ring_position(rotor):
    assert rotor.ring_position == 0


def test_has_rotational_position(rotor):
    assert rotor.rotational_position == 0


@pytest.mark.parametrize(
    "rotational_position,ring_position,input,expected",
    (
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 0, 25, 25),
        (0, 1, 0, 25),
        (0, 1, 2, 1),
        (0, 1, 25, 24),
        (0, 1, 24, 23),
        (0, 25, 0, 1),
        (0, 25, 1, 2),
        (0, 25, 2, 3),
        (1, 0, 0, 1),
        (1, 0, 1, 2),
        (1, 0, 25, 0),
        (1, 1, 0, 0),
        (1, 1, 25, 25),
        (25, 0, 0, 25),
    ),
)
def test_position_to_wire(rotational_position, ring_position, input, expected, rotor):
    rotor.rotational_position = rotational_position
    rotor.ring_position = ring_position
    assert rotor._position_to_wire(input) == expected


@pytest.mark.parametrize(
    "rotational_position,ring_position,input,expected",
    (
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 0, 25, 25),
        (0, 1, 25, 0),
        (0, 1, 1, 2),
        (0, 1, 24, 25),
        (0, 1, 23, 24),
        (0, 25, 1, 0),
        (0, 25, 2, 1),
        (0, 25, 3, 2),
        (1, 0, 1, 0),
        (1, 0, 2, 1),
        (1, 0, 0, 25),
        (1, 1, 0, 0),
        (1, 1, 25, 25),
        (25, 0, 25, 0),
    ),
)
def test_wire_to_position(rotational_position, ring_position, input, expected, rotor):
    rotor.rotational_position = rotational_position
    rotor.ring_position = ring_position
    assert rotor._wire_to_position(input) == expected


@pytest.mark.parametrize(
    "ring_position,input,output",
    (
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 1, 1),
    ),
)
def test_straight_rotor(ring_position, input, output):
    rotor = Rotor(
        wiring=list(range(27)),
        ring_position=ring_position,
        notches=(0,),
    )
    assert rotor.right_to_left(input) == output
    assert rotor.left_to_right(output) == input


@pytest.mark.parametrize(
    "ring_position,input,output",
    (
        (0, 0, 4),
        (0, 4, 11),
        (0, 1, 10),
        (0, 25, 9),
        (1, 0, 10),
    ),
)
def test_rotor_I(ring_position, input, output, rotor_I_wiring):
    rotor = Rotor(
        wiring=rotor_I_wiring,
        ring_position=ring_position,
        notches=(0,),
    )
    assert rotor.right_to_left(input) == output
    assert rotor.left_to_right(output) == input


@pytest.mark.parametrize("position,expected", ((0, 1), (1, 2), (24, 25), (25, 0)))
def test_rotate(position, expected, rotor):
    rotor.rotational_position = position
    rotor.rotate()
    assert rotor.rotational_position == expected


def test_wiring_string():
    rotor = Rotor(wiring=list(range(26)), notches=[])
    assert rotor.wiring_string() == ascii_uppercase


def test_notches_string():
    rotor = Rotor(wiring=list(range(26)), notches=[0, 23])
    assert rotor.notches_string() == "AX"


def test_ring_setting_string():
    rotor = Rotor(wiring=list(range(26)), notches=[], ring_position=5)
    assert rotor.ring_setting_string() == "6"


def test_position_string():
    rotor = Rotor(wiring=list(range(26)), notches=[])
    rotor.rotational_position = 5
    assert rotor.position_string() == "F"


def test_repr():
    rotor = Rotor(wiring=list(range(26)), notches=[0, 23], ring_position=5)
    rotor.rotational_position = 5
    assert repr(rotor) == "<Rotor: ABCDEFGHIJKLMNOPQRSTUVWXYZ - AX - 6 - F>"
