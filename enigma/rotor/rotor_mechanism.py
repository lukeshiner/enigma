"""The RotorController class."""

import logging
from string import ascii_uppercase as alphabet
from typing import Optional, Sequence

from .reflector import Reflector
from .rotor import Rotor

logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


class RotorMechanism:
    """Controller for Enigma's rotors."""

    def __init__(
        self,
        rotors: Optional[Sequence[Rotor]] = None,
        reflector: Optional[Reflector] = None,
    ):
        """Set up enimga's rotors."""
        if rotors is None:
            self.rotors: Sequence[Rotor] = []
        else:
            self.rotors = rotors
        if reflector is None:
            reflector = Reflector(wiring=alphabet)
        self.reflector = reflector

    def encode(self, value: str) -> str:
        """Return value encoded by rotors."""
        self.update_rotor_positions()
        first_pass_value = self.encode_rotor_right_left(len(self.rotors) - 1, value)
        reflector_value = self.reflector.encode(first_pass_value)
        logging.debug("Reflector encoded {} to {}".format(value, reflector_value))
        encoded_value = self.encode_rotor_left_right(0, reflector_value)
        logging.info("Encoded {} to {}".format(value, encoded_value))
        return encoded_value

    def encode_rotor_right_left(self, rotor_position: int, value: str) -> str:
        """Return right to left encoding of the rotor."""
        encoded_value = self.rotors[rotor_position].encode(value)
        logging.debug(
            "Rotor {} encoded {} < {}".format(rotor_position, value, encoded_value)
        )
        if rotor_position == 0:
            return encoded_value
        return self.encode_rotor_right_left(rotor_position - 1, encoded_value)

    def encode_rotor_left_right(self, rotor_position: int, value: str) -> str:
        """Return left to right encoding of the rotor."""
        encoded_value = self.rotors[rotor_position].encode(value, reverse=True)
        logging.debug(
            "Rotor {} encoded {} > {}".format(rotor_position, value, encoded_value)
        )
        if rotor_position == len(self.rotors) - 1:
            return encoded_value
        return self.encode_rotor_left_right(rotor_position + 1, encoded_value)

    def update_rotor_positions(self) -> None:
        """Update the rotation of the rotors."""
        self.rotors[-1].rotate()
        for rotor_position in reversed(range(0, len(self.rotors) - 1)):
            if self.rotors[rotor_position + 1].rotate_next_rotor():
                self.rotors[rotor_position].rotate()
