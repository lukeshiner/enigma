"""Tests for the enigma module."""

import unittest

from enigma import Enigma


class TestEnigma(unittest.TestCase):
    """Tests for the enigma class."""

    def get_enigma(
        self,
        rotors=[
            {
                "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": ["R"],
            },
            {
                "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": ["F"],
            },
            {
                "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                "position": "A",
                "ring_setting": 1,
                "turnover_positions": ["W"],
            },
        ],
        reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT",
        plugboard=[],
    ):
        """Test enigma object can be created."""
        return Enigma(rotors=rotors, reflector=reflector, plugboard=plugboard)

    def test_enigma_default_encoding(self):
        """Test enigma encoding with default setup."""
        enigma = self.get_enigma()
        self.assertEqual(enigma.encode("HELL OWOR LD"), "ILBD AAMT AZ")
