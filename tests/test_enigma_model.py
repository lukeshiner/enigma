from unittest import mock

import pytest

from enigma.enigma_model import EnigmaModel


@pytest.fixture
def enigma():
    return EnigmaModel()


@pytest.fixture
def mock_enimga_model_super():
    with mock.patch("enigma.enigma_model.super") as m:
        yield m


def test_set_reflector(mock_enimga_model_super, enigma):
    enigma.available_reflectors = {"A": mock.Mock()}
    enigma.set_reflector("A")
    mock_enimga_model_super.return_value.set_reflector.assert_called_once_with(
        enigma.available_reflectors["A"].return_value
    )


def test_set_rotors(mock_enimga_model_super, enigma):
    enigma.available_rotors = {key: mock.Mock() for key in ("I", "II", "III")}
    enigma.set_rotors("I II III")
    mock_enimga_model_super.return_value.set_rotors.assert_called_once_with(
        [
            enigma.available_rotors["I"].return_value,
            enigma.available_rotors["II"].return_value,
            enigma.available_rotors["III"].return_value,
        ]
    )


def test_set_ring_settings(mock_enimga_model_super, enigma):
    enigma.set_ring_settings("1 05 26")
    mock_enimga_model_super.return_value.set_ring_settings.assert_called_once_with(
        [0, 4, 25]
    )


def test_set_ring_settings_with_empty_value(mock_enimga_model_super, enigma):
    enigma.rotor_count = 3
    enigma.set_ring_settings("")
    mock_enimga_model_super.return_value.set_ring_settings.assert_called_once_with(
        [0, 0, 0]
    )


def test_set_rotor_positions(mock_enimga_model_super, enigma):
    enigma.set_rotor_positions("ACZ")
    mock_enimga_model_super.return_value.set_rotor_positions.assert_called_once_with(
        [0, 2, 25]
    )


def test_set_plugboard(mock_enimga_model_super, enigma):
    enigma.set_plugboard("AZ CD")
    mock_enimga_model_super.return_value.set_plugboard.assert_called_once_with(
        ((0, 25), (2, 3))
    )


def test_setup(enigma):
    enigma.set_rotors = mock.Mock()
    enigma.set_reflector = mock.Mock()
    enigma.set_ring_settings = mock.Mock()
    enigma.set_rotor_positions = mock.Mock()
    enigma.set_plugboard = mock.Mock()
    enigma.setup(
        rotors="I II III",
        reflector="B",
        ring_settings="01 05 03",
        starting_positions="ABZ",
        plugboard_pairs="AB YZ",
    )
    enigma.set_rotors.assert_called_once_with("I II III")
    enigma.set_reflector.assert_called_once_with("B")
    enigma.set_ring_settings.assert_called_once_with("01 05 03")
    enigma.set_rotor_positions.assert_called_once_with("ABZ")
    enigma.set_plugboard.assert_called_once_with("AB YZ")
