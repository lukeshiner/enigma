"""Encoders for enigma's rotor mechanism."""

from . import exceptions
from .encoder import Encoder


class Rotor(Encoder):
    """
    Enigma's Rotors.

    Attributes:
        wriring:
            The pin connections of the rotor.

        ring_setting:
            The ring setting of the rotor.

        position:
            The current position of the rotor.

    """

    def __init__(
            self,
            wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            ring_setting='01',
            position='A'):
        """
        Set the initial settings of the rotor.

        Kwargs:

            wiring:
                String containing the letters the pins on the right side
                will connect to for each left hand pin when the rotor is in
                position 'A'.

            ring_offset:
                The offset of the letters on the rotor as a letter or number.
                Default: 'A'.

            position:
                The starting position of the rotor as a letter or number.
                Default: 'A'.

        """
        super().__init__(wiring)
        self.ring_offset = self._get_rotation_offset(ring_setting)
        self.set_position(self._get_rotation_offset(position))

    def encode(self, letter, reverse=False):
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
        pin_number = self._find_pin(letter)
        if reverse is True:
            pin_location = self.wiring.right_pin(pin_number)
        else:
            pin_location = self.wiring.left_pin(pin_number)
        return self._find_letter(pin_location)

    def rotate(self, turns=1):
        """
        Rotate the rotor.

        Args:
            turns: Number of times to rotate the rotor. Default: 1.
        """
        self.rotation += turns
        if self.rotation >= len(self.wiring):
            self.rotation = 0

    def set_position(self, position):
        """Turn the rotor to a given position."""
        offset = position - self.ring_offset
        if offset < 0:
            offset += len(self.wiring)
        self.rotation = offset

    @property
    def position(self):
        """Return the current position of the rotor."""
        offset = self.rotation + self.ring_offset
        if offset >= len(self.wiring):
            offset -= len(self.wiring)
        return self.ALPHA[offset]

    @property
    def ring_setting(self):
        """
        Return the current ring setting.

        Returns:
            str containg a two digit, zero padded integer.

        """
        return str(self.ring_offset + 1).zfill(2)

    def _find_pin(self, pin_letter):
        """Return the pin number for a given letter input."""
        pin_position = self.ALPHA.index(pin_letter)
        offset = pin_position + self.rotation
        if offset >= len(self.wiring):
            offset -= len(self.wiring)
        return offset

    def _find_letter(self, pin_number):
        """Find the letter position for a given pin number."""
        offset = pin_number - self.rotation
        return self.ALPHA[offset]

    def _get_rotation_offset(self, input):
        """Return a rotational offset from a str or in input."""
        if isinstance(input, int):
            return self._get_rotation_offset_numeric(input)
        if isinstance(input, str):
            return self._get_rotation_offset_alpha(input)
        raise exceptions.InvalidRotorSetting(input)

    def _get_rotation_offset_numeric(self, position: int):
        """Set rotor position with numeric input."""
        if position > len(self.wiring):
            raise exceptions.InvalidRotorSetting(position)
        return position - 1

    def _get_rotation_offset_alpha(self, position: str):
        """Set rotor position for string input."""
        if position.isdigit():
            return self._get_rotation_offset_numeric(int(position))
        try:
            numeric_position = self.ALPHA.index(position.upper())
        except ValueError as e:
            raise exceptions.InvalidRotorSetting(position)
        return numeric_position
