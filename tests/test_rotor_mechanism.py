from unittest import mock

import pytest

from enigma.enigma_machine import Reflector, Rotor, RotorMechanism


@pytest.fixture
def rotors():
    return [Rotor(wiring=range(26), notches=(25,)) for _ in range(3)]


@pytest.fixture
def reflector():
    return Reflector(wiring=range(26))


@pytest.fixture
def rotor_mechanism(rotors, reflector):
    return RotorMechanism(rotors=rotors, reflector=reflector)


def test_update_rotor_positions_moves_first_rotor(rotor_mechanism):
    rotor = rotor_mechanism.rotors[2]
    rotor.rotational_position = 0
    rotor_mechanism.update_rotor_positions()
    assert rotor.rotational_position == 1


def test_update_rotor_positions_moves_second_rotor(rotor_mechanism):
    rotor_mechanism.rotors[2].rotational_position = 0
    rotor_mechanism.rotors[2].notches = {1}
    rotor_mechanism.rotors[1].rotational_position = 0
    rotor_mechanism.update_rotor_positions()
    assert rotor_mechanism.rotors[1].rotational_position == 1


def test_update_rotor_positions_moves_third_rotor(rotor_mechanism):
    rotor_mechanism.rotors[2].rotational_position = 0
    rotor_mechanism.rotors[2].notches = {1}
    rotor_mechanism.rotors[1].rotational_position = 0
    rotor_mechanism.rotors[1].notches = {1}
    rotor_mechanism.rotors[0].rotational_position = 0
    rotor_mechanism.update_rotor_positions()
    assert rotor_mechanism.rotors[0].rotational_position == 1


def test_update_rotor_positions_does_not_move_second_rotor(rotor_mechanism):
    rotor_mechanism.rotors[2].rotational_position = 0
    rotor_mechanism.rotors[2].notches = {17}
    rotor_mechanism.rotors[1].rotational_position = 0
    rotor_mechanism.update_rotor_positions()
    assert rotor_mechanism.rotors[1].rotational_position == 0


def test_update_rotor_positions_does_not_move_third_rotor(rotor_mechanism):
    rotor_mechanism.rotors[2].rotational_position = 0
    rotor_mechanism.rotors[2].notches = {1}
    rotor_mechanism.rotors[1].rotational_position = 0
    rotor_mechanism.rotors[1].notches = {17}
    rotor_mechanism.rotors[0].rotational_position = 0
    rotor_mechanism.update_rotor_positions()
    assert rotor_mechanism.rotors[1].rotational_position == 1
    assert rotor_mechanism.rotors[0].rotational_position == 0


def test_encode(rotor_mechanism):
    rotor_mechanism.rotors = [mock.Mock() for _ in range(3)]
    rotor_mechanism.reflector = mock.Mock()
    return_value = rotor_mechanism.encode(0)
    rotor_mechanism.rotors[2].right_to_left.assert_called_once_with(0)
    rotor_mechanism.rotors[1].right_to_left.assert_called_once_with(
        rotor_mechanism.rotors[2].right_to_left.return_value
    )
    rotor_mechanism.rotors[0].right_to_left.assert_called_once_with(
        rotor_mechanism.rotors[1].right_to_left.return_value
    )
    rotor_mechanism.reflector.connection.assert_called_once_with(
        rotor_mechanism.rotors[0].right_to_left.return_value
    )
    rotor_mechanism.rotors[0].left_to_right.assert_called_once_with(
        rotor_mechanism.reflector.connection.return_value
    )
    rotor_mechanism.rotors[1].left_to_right.assert_called_once_with(
        rotor_mechanism.rotors[0].left_to_right.return_value
    )
    rotor_mechanism.rotors[2].left_to_right.assert_called_once_with(
        rotor_mechanism.rotors[1].left_to_right.return_value
    )
    assert return_value == rotor_mechanism.rotors[2].left_to_right.return_value


def test_set_positions(rotor_mechanism):
    rotor_mechanism.set_positions([3, 25, 8])
    assert rotor_mechanism.rotors[0].rotational_position == 3
    assert rotor_mechanism.rotors[1].rotational_position == 25
    assert rotor_mechanism.rotors[2].rotational_position == 8


def test_set_ring_settings(rotor_mechanism):
    rotor_mechanism.set_ring_settings([22, 4, 17])
    assert rotor_mechanism.rotors[0].ring_position == 22
    assert rotor_mechanism.rotors[1].ring_position == 4
    assert rotor_mechanism.rotors[2].ring_position == 17
