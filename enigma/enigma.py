"""Base class for Enigma machines."""

from string import ascii_uppercase as alphabet
from typing import List, Sequence

from .plugboard import Plugboard
from .rotor import Reflector, Rotor, RotorMechanism


class Enigma:
    """Base class for Enigma machines."""

    def __init__(
        self, *, rotors: Sequence[Rotor], reflector: Reflector, plugboard: Plugboard
    ):
        """Create enigma setup."""
        self.rotor_mechanism = RotorMechanism(rotors=rotors, reflector=reflector)
        self.plugboard = plugboard

    def encode(self, plain_text: str, blocks: int = 4) -> str:
        """Encode message."""
        prepared_plain_text = self.prepare_input(plain_text)
        raw_output = [self.encode_letter(letter) for letter in prepared_plain_text]
        output = self.format_output(raw_output, blocks=blocks)
        return output

    def encode_letter(self, letter: str) -> str:
        """Encypher a single letter with the enigma machine."""
        return self.plugboard.encode(
            self.rotor_mechanism.encode(self.plugboard.encode(letter))
        )

    def prepare_input(self, input: str) -> str:
        """Format input message as a string of uppercase letters."""
        input = input.upper()
        invalid_characters = [letter for letter in input if letter not in alphabet]
        for letter in invalid_characters:
            input = input.replace(letter, "")
        return input

    def format_output(self, output: List[str], blocks: int = 4) -> str:
        """Format the output message into blocks of four uppercase letters."""
        block_text = self.split_into_blocks(output, blocks)
        return block_text.upper()

    def split_into_blocks(self, input: List[str], block_size: int) -> str:
        """Split iterable into blocks."""
        blocks = [input[i : i + block_size] for i in range(0, len(input), block_size)]
        text_blocks = ["".join(block) for block in blocks]
        text = " ".join(text_blocks)
        return text

    def reset(self) -> None:
        """Reset to starting settings."""
        self.rotor_mechanism.reset()
