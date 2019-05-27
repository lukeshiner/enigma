"""Encoders for enigma's rotor mechanism."""

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
        wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        ring_setting=1,
        position="A",
        turnover_positions=["R"],
    ):
        """
        Set the initial settings of the rotor.

        Kwargs:

            wiring:
                String containing the letters the pins on the right side
                will connect to for each left hand pin when the rotor is in
                position 'A'.

            ring_setting:
                The offset of the letters on the rotor as a letter or number.
                Default: 'A'.

            position:
                The starting position of the rotor as a letter or number.
                Default: 'A'.

            turnover_positions:
                String or list of strings containig the letter position at
                which the rotor will cause the next to rotate. Default: 'A'.

        """
        super().__init__(wiring)
        self.turnover_positions = turnover_positions
        self.ring_setting = ring_setting
        self.set_position(position)

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

    def set_position(self, letter_position):
        """Turn the rotor to a given position."""
        numeric_position = self.ALPHA.index(letter_position) + 1
        offset = numeric_position - self.ring_setting
        if offset < 0:
            offset += len(self.wiring)
        self.rotation = offset

    def rotate_next_rotor(self):
        """Return True if the next rotor should rotate."""
        if self.position in self.turnover_positions:
            return True
        return False

    @property
    def position(self):
        """Return the current position of the rotor."""
        offset = self.rotation + self.ring_setting - 1
        if offset >= len(self.wiring):
            offset -= len(self.wiring)
        return self.ALPHA[offset]

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
