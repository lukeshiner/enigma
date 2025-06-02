from unittest import mock as mock

import pytest

from enigma.enigma_model import EnigmaI


@pytest.fixture
def mock_enimga_model_super():
    with mock.patch("enigma.enigma_model.super") as m:
        yield m


@pytest.fixture
def enigma():
    return EnigmaI()


def test_setup(enigma):
    enigma.set_rotors = mock.Mock()
    enigma.set_reflector = mock.Mock()
    enigma.set_ring_settings = mock.Mock()
    enigma.set_rotor_positions = mock.Mock()
    enigma.set_plugboard = mock.Mock()
    enigma.setup(
        rotors="I II III",
        ring_settings="01 05 03",
        starting_positions="ABZ",
        plugboard_pairs="AB YZ",
    )
    enigma.set_rotors.assert_called_once_with("I II III")
    enigma.set_reflector.assert_called_once_with("A")
    enigma.set_ring_settings.assert_called_once_with("01 05 03")
    enigma.set_rotor_positions.assert_called_once_with("ABZ")
    enigma.set_plugboard.assert_called_once_with("AB YZ")
