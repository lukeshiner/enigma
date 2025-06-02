from unittest import mock

import pytest

from enigma.enigma_machine import EnigmaMachine


@pytest.fixture
def enigma_machine():
    return EnigmaMachine()


@pytest.fixture
def mock_rotor_mechanism(enigma_machine):
    enigma_machine.rotor_mechanism = mock.Mock()
    return enigma_machine.rotor_mechanism


@pytest.fixture
def mock_plugboard(enigma_machine):
    enigma_machine.plugboard = mock.Mock()
    return enigma_machine.plugboard


def test_enigma_machine_has_rotor_mechanism(enigma_machine):
    assert isinstance(
        enigma_machine.rotor_mechanism, enigma_machine.rotor_mechanism_class
    )


def test_enigma_machine_has_plugboard(enigma_machine):
    assert isinstance(enigma_machine.plugboard, enigma_machine.plugboard_class)


def test_set_rotors(enigma_machine):
    rotors = [mock.Mock() for _ in range(3)]
    enigma_machine.set_rotors(rotors)
    assert enigma_machine.rotor_mechanism.rotors == rotors


def test_set_reflector(enigma_machine):
    reflector = mock.Mock()
    enigma_machine.set_reflector(reflector)
    assert enigma_machine.rotor_mechanism.reflector == reflector


def test_set_ring_settings(enigma_machine, mock_rotor_mechanism):
    positions = [22, 4, 17]
    enigma_machine.set_ring_settings(positions)
    mock_rotor_mechanism.set_ring_settings.assert_called_once_with(positions)


def test_set_rotor_positions(enigma_machine, mock_rotor_mechanism):
    positions = [22, 4, 17]
    enigma_machine.set_rotor_positions(positions)
    mock_rotor_mechanism.set_positions.assert_called_once_with(positions)


def test_set_plugboard_pairs(enigma_machine, mock_plugboard):
    pairs = ((22, 11), (17, 8))
    enigma_machine.set_plugboard(pairs)
    mock_plugboard.set_pairs.assert_called_once_with(pairs)


def test_int_encode(enigma_machine, mock_rotor_mechanism):
    enigma_machine._encode_key = mock.Mock()
    enigma_machine._int_encode(5)
    mock_rotor_mechanism.update_rotor_positions.assert_called_once_with()
    enigma_machine._encode_key.assert_called_once_with(5)


def test_encode_key(enigma_machine, mock_plugboard, mock_rotor_mechanism):
    return_value = enigma_machine._encode_key(5)
    assert return_value == mock_plugboard.encode.return_value
    mock_plugboard.encode.assert_has_calls(
        (mock.call(5), mock.call(mock_rotor_mechanism.encode.return_value)),
        any_order=False,
    )
    mock_rotor_mechanism.encode.assert_called_once_with(
        mock_plugboard.encode.return_value
    )


def test_string_to_ints(enigma_machine):
    assert enigma_machine._string_to_ints("AB C 1 ?") == [0, 1, 2]


def test_ints_to_string(enigma_machine):
    assert enigma_machine._ints_to_string([0, 1, 2]) == "ABC"


@pytest.mark.parametrize(
    "text,block_size,expected",
    (
        ("helloworld", 0, "helloworld"),
        ("helloworld", 5, "hello world"),
        ("helloworld", 4, "hell owor ld"),
    ),
)
def test_to_blocks(text, block_size, expected):
    assert EnigmaMachine.to_blocks(text, block_size=block_size) == expected


@pytest.fixture
def mock_string_to_ints(enigma_machine):
    enigma_machine._string_to_ints = mock.Mock(return_value=[])
    return enigma_machine._string_to_ints


@pytest.fixture
def mock_ints_to_string(enigma_machine):
    enigma_machine._ints_to_string = mock.Mock()
    return enigma_machine._ints_to_string


@pytest.fixture
def mock_int_encode(enigma_machine):
    enigma_machine._int_encode = mock.Mock()
    return enigma_machine._int_encode


def test_encode_calls_string_to_ints(
    enigma_machine, mock_string_to_ints, mock_ints_to_string, mock_int_encode
):
    enigma_machine.encode("ABC")
    mock_string_to_ints.assert_called_once_with("ABC")


def test_encode_calls_int_encode(
    enigma_machine, mock_string_to_ints, mock_ints_to_string, mock_int_encode
):
    mock_string_to_ints.return_value = [0, 1, 2]
    enigma_machine.encode("ABC")
    mock_int_encode.assert_has_calls(
        (mock.call(0), mock.call(1), mock.call(2)), any_order=False
    )


def test_encode_calls_ints_to_string(
    enigma_machine, mock_string_to_ints, mock_ints_to_string, mock_int_encode
):
    mock_string_to_ints.return_value = [0, 1, 2]
    mock_int_encode.side_effect = [0, 1, 2]
    enigma_machine.encode("ABC")
    mock_ints_to_string.assert_called_once_with([0, 1, 2])


def test_encode_returns_text(
    enigma_machine, mock_string_to_ints, mock_ints_to_string, mock_int_encode
):
    return_value = enigma_machine.encode("ABC")
    assert return_value == mock_ints_to_string.return_value
