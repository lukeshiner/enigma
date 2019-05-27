"""Base class for rotor tests."""

import unittest

from enigma.rotor.reflector import Reflector
from enigma.rotor.rotor import Rotor


class RotorTest(unittest.TestCase):
    """Provides tools testing rotors."""

    def get_rotor(
        self,
        wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        ring_setting=1,
        position="A",
        turnover_positions=["R"],
    ):
        """Return Rotor object."""
        return Rotor(
            wiring=wiring,
            ring_setting=ring_setting,
            position=position,
            turnover_positions=turnover_positions,
        )

    def get_reflector(self, wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT"):
        """Return Reflector object."""
        return Reflector(wiring=wiring)
