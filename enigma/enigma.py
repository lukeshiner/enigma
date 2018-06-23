"""Base class for Enigma machines."""
from .plugboard import Plugboard
from .rotor import Reflector, Rotor, RotorMechanism


class Enigma:
    """Base class for Enigma machines."""

    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, rotors=[], reflector='', plugboard=[]):
        """Create enigma setup."""
        rotors = [self.get_rotor(rotor) for rotor in rotors]
        if isinstance(reflector, Reflector):
            reflector = reflector
        else:
            reflector = Reflector(wiring=reflector)
        self.rotors = RotorMechanism(rotors=rotors, reflector=reflector)
        if isinstance(plugboard, Plugboard):
            self.plugboard = plugboard
        else:
            self.plugboard = Plugboard(plugboard)

    def get_rotor(self, rotor):
        """Get Rotor instance."""
        if isinstance(rotor, Rotor):
            return rotor
        if isinstance(rotor, dict):
            return Rotor(**rotor)
        else:
            return Rotor(*rotor)

    def encode(self, plain_text):
        """Encode message."""
        prepared_plain_text = self.prepare_input(plain_text)
        raw_output = [
            self.encode_letter(letter) for letter in prepared_plain_text
        ]
        output = self.format_output(raw_output)
        return output

    def encode_letter(self, letter):
        """Encypher a single letter with the enigma machine."""
        return self.plugboard.encode(
            self.rotors.encode(self.plugboard.encode(letter)))

    def prepare_input(self, input):
        """Format input message as a string of uppercase letters."""
        input = input.upper()
        invalid_characters = [
            letter for letter in input if letter not in self.ALPHA
        ]
        for letter in invalid_characters:
            input = input.replace(letter, '')
        return input

    def format_output(self, output):
        """Format the output message into blocks of four uppercase letters."""
        block_text = self.split_into_blocks(output, 4)
        return block_text.upper()

    def split_into_blocks(self, input, block_size):
        """Split iterable into blocks."""
        blocks = [
            input[i:i + block_size] for i in range(0, len(input), block_size)
        ]
        text_blocks = [''.join(block) for block in blocks]
        text = ' '.join(text_blocks)
        return text
