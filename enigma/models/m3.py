"""Specific Enigma models."""

from enigma.rotor import Rotor
from enigma.rotor.reflector import Reflector

from .enigma_model import EnigmaModel

rotors = {
    "I": Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", turnover_positions="R"),
    "II": Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", turnover_positions="F"),
    "III": Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", turnover_positions="W"),
    "IV": Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", turnover_positions="K"),
    "V": Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", turnover_positions="A"),
    "VI": Rotor(wiring="JPGVOUMFYQBENHZRDKASXLICTW", turnover_positions="AN"),
    "VII": Rotor(wiring="NZJHGRCXMYSWBOUFAIVLPEKQDT", turnover_positions="AN"),
    "VIII": Rotor(wiring="FKQHTLXOCBJSPDZRAMEWNIUYGV", turnover_positions="AN"),
}

reflectors = {
    "A": Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL"),
}


class M3(EnigmaModel):
    """The M3 Enigma."""

    name = "M3"

    available_rotors = dict(rotors)
    available_reflectors = dict(reflectors)
    rotor_count = 3


class M3Army(M3):
    """The Army M3 Enigma."""

    name = "M3 Army"

    available_rotors = {
        "I": rotors["I"],
        "II": rotors["II"],
        "III": rotors["III"],
        "IV": rotors["IV"],
        "V": rotors["V"],
    }

    available_reflectors = {"A": reflectors["A"]}
    rotor_count = 3
