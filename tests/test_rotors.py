from string import ascii_uppercase
from unittest import mock

import pytest

from enigma import rotors


@mock.patch("enigma.rotors.Rotor")
def test_make_rotor(mock_rotor_class):
    wiring = str(ascii_uppercase)
    notches = "AZ"
    return_value = rotors.make_rotor(wiring=wiring, notches=notches)
    assert return_value == mock_rotor_class.return_value
    mock_rotor_class.assert_called_once_with(wiring=list(range(26)), notches=[0, 25])


@mock.patch("enigma.rotors.Reflector")
def test_make_reflector(mock_reflector_class):
    wiring = str(ascii_uppercase)
    return_value = rotors.make_reflector(wiring=wiring)
    assert return_value == mock_reflector_class.return_value
    mock_reflector_class.assert_called_once_with(wiring=list(range(26)))


@pytest.fixture
def rotor_test():
    def _rotor_test(rotor_method, wiring, notches):
        rotor = rotor_method()
        assert rotor.wiring == [ascii_uppercase.index(char) for char in wiring]
        assert rotor.notches == set([ascii_uppercase.index(char) for char in notches])

    return _rotor_test


@pytest.fixture
def reflector_test():
    def _reflector_test(rotor_method, wiring):
        rotor = rotor_method()
        assert rotor.wiring == [ascii_uppercase.index(char) for char in wiring]

    return _reflector_test


def test_rotor_I(rotor_test):
    rotor_test(
        rotors.rotor_I,
        wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        notches="R",
    )


def test_rotor_II(rotor_test):
    rotor_test(
        rotors.rotor_II,
        wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE",
        notches="F",
    )


def test_rotor_III(rotor_test):
    rotor_test(
        rotors.rotor_III,
        wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO",
        notches="W",
    )


def test_rotor_IV(rotor_test):
    rotor_test(
        rotors.rotor_IV,
        wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB",
        notches="K",
    )


def test_rotor_V(rotor_test):
    rotor_test(
        rotors.rotor_V,
        wiring="VZBRGITYUPSDNHLXAWMJQOFECK",
        notches="A",
    )


def test_rotor_VI(rotor_test):
    rotor_test(
        rotors.rotor_VI,
        wiring="JPGVOUMFYQBENHZRDKASXLICTW",
        notches="AN",
    )


def test_rotor_VII(rotor_test):
    rotor_test(
        rotors.rotor_VII,
        wiring="NZJHGRCXMYSWBOUFAIVLPEKQDT",
        notches="AN",
    )


def test_rotor_VIII(rotor_test):
    rotor_test(
        rotors.rotor_VIII,
        wiring="FKQHTLXOCBJSPDZRAMEWNIUYGV",
        notches="AN",
    )


def test_reflector_A(reflector_test):
    reflector_test(rotors.reflector_A, wiring="EJMZALYXVBWFCRQUONTSPIKHGD")


def test_reflector_B(reflector_test):
    reflector_test(rotors.reflector_B, wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")


def test_reflector_C(reflector_test):
    reflector_test(rotors.reflector_C, wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")
