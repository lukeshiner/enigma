"""Reflectors for enigma."""

from .encoder import Encoder


class Reflector(Encoder):
    """Base class for reflectors."""

    def encode(self, input):
        """
        Return the letter position currently connected to annother.

        The letter positions are those of a rotor in position 'A' with a ring
        setting of 01.

        Args:
            letter:
                The input position.

        Kwargs:
            reverse:
                If True the encoding is left to right, otherwise right to left.
                Default: False.

        Returns:
            The letter position of the pin connected to the one at the passed
            letter postion.

        """
        input_pin = self._find_pin(input)
        output_pin = self.wiring.right_pin(input_pin)
        return self._find_letter(output_pin)

    def _find_pin(self, pin_letter):
        """Return the pin number for a given letter input."""
        return self.ALPHA.index(pin_letter)

    def _find_letter(self, pin_number):
        """Find the letter position for a given pin number."""
        return self.ALPHA[pin_number]
