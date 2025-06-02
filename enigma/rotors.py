"""Enigma rotors and reflectors."""

from string import ascii_uppercase

from .enigma_machine import Reflector, Rotor


def make_rotor(wiring, notches):
    """Return a rotor instance."""
    wiring = [ascii_uppercase.index(char) for char in wiring]
    notches = [ascii_uppercase.index(char) for char in notches]
    return Rotor(wiring=wiring, notches=notches)


def make_reflector(wiring):
    """Return a rotor instance."""
    wiring = [ascii_uppercase.index(char) for char in wiring]
    return Reflector(wiring=wiring)


def rotor_I():
    """Return Rotor I."""
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    notches = "R"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_II():
    """Return Rotor II."""
    wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    notches = "F"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_III():
    """Return Rotor III."""
    wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    notches = "W"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_IV():
    """Return Rotor IV."""
    wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    notches = "K"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_V():
    """Return Rotor V."""
    wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
    notches = "A"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_VI():
    """Return Rotor VI."""
    wiring = "JPGVOUMFYQBENHZRDKASXLICTW"
    notches = "AN"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_VII():
    """Return Rotor VII."""
    wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
    notches = "AN"
    return make_rotor(wiring=wiring, notches=notches)


def rotor_VIII():
    """Return Rotor VIII."""
    wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
    notches = "AN"
    return make_rotor(wiring=wiring, notches=notches)


def reflector_A():
    """Return Reflector A."""
    return make_reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")


def reflector_B():
    """Return Reflector B."""
    return make_reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")


def reflector_C():
    """Return Reflector C."""
    return make_reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")
