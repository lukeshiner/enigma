"""Tests for engima's rotor mechanism."""

import string
import unittest

from enigma import Reflector, Rotor, RotorMechanism


class TestRotorMechanism(unittest.TestCase):
    """Test class for enigma's rotor mechanism."""

    def get_rotors(self, settings):
        """Return rotor set."""
        return [Rotor(**setting) for setting in settings]

    def get_rotor_mechanism(
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
        reflector=Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    ):
        """Return rotor mechanism."""
        rotors = self.get_rotors(rotors)
        return RotorMechanism(rotors=rotors, reflector=reflector)

    def test_default_position_encoding(self):
        """
        Test the rotor mechanism returns correct.

        Input string: 'AAA'
        Rotor position 1: Rotor I
        Rotor position 2: Rotor II
        Rotor position 3: Rotor III

        All rotors in position A with ring setting of 01.
        """
        rotors = self.get_rotor_mechanism()
        self.assertEqual("".join([rotors.encode(l) for l in "AAA"]), "BDZ")

    def test_first_rotor_rotates(self):
        """Test that the first rotor rotates after a keypress."""
        rotors = self.get_rotor_mechanism()
        self.assertEqual(rotors.rotors[2].position, "A")
        rotors.encode("A")
        self.assertEqual(rotors.rotors[2].position, "B")
        rotors.encode("A")
        self.assertEqual(rotors.rotors[2].position, "C")

    def test_second_rotor_rotates(self):
        """Test that the second rotor rotates."""
        rotors = self.get_rotor_mechanism()
        rotors.rotors[2].set_position("V")
        self.assertEqual(rotors.rotors[2].turnover_positions, ["W"])
        self.assertEqual(rotors.rotors[1].position, "A")
        rotors.encode("A")
        self.assertEqual(rotors.rotors[2].position, "W")
        self.assertEqual(rotors.rotors[1].position, "B")

    def test_rotor_mechanism_without_a_reflector(self):
        """Test a rotor mechanism can be instaniated without a reflector."""
        rotors = self.get_rotor_mechanism(reflector=None)
        reflector = rotors.reflector
        for letter in string.ascii_uppercase:
            self.assertEqual(reflector.encode(letter), letter)
