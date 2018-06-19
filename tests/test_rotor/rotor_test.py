"""Base class for rotor tests."""

from enigma.rotor.reflector import Reflector
from enigma.rotor.rotor import Rotor


class RotorTest:
    """Provides tools testing rotors."""

    def get_rotor(
            self,
            wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            ring_setting='01',
            position='A'):
        """Return Rotor object."""
        return Rotor(
            wiring=wiring, ring_setting=ring_setting, position=position)

    def get_reflector(self, wiring='YRUHQSLDPXNGOKMIEBFZCWVJAT'):
        """Return Reflector object."""
        return Reflector(wiring=wiring)
