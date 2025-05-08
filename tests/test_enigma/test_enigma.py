"""Tests for the enigma module."""

import unittest

from enigma import Enigma, Plugboard, Reflector, Rotor


class TestEnigma(unittest.TestCase):
    """Tests for the enigma class."""

    def get_enigma(
        self,
        rotors=[
            {
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": "R",
            },
            {
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": "F",
            },
            {
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": "W",
            },
        ],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard=[],
    ):
        """Test enigma object can be created."""
        used_rotors = [
            Rotor(
                wiring=_["wiring"],
                start_position=_["position"],
                ring_setting=_["ring_setting"],
                turnover_positions=_["turnover_positions"],
            )
            for _ in rotors
        ]
        used_reflector = Reflector(wiring=reflector)
        used_plugboard = Plugboard(plugboard)
        return Enigma(
            rotors=used_rotors, reflector=used_reflector, plugboard=used_plugboard
        )

    def test_enigma_default_encoding(self):
        """Test enigma encoding with default setup."""
        enigma = self.get_enigma()
        self.assertEqual(enigma.encode("HELL OWOR LD"), "ILBD AAMT AZ")
