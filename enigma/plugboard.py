"""Enigma's Plugboard."""
from string import ascii_uppercase as alphabet
from typing import Dict, Optional, Sequence, Tuple


class Plugboard:
    """Enigma's Plugboard."""

    def __init__(self, connections: Optional[Sequence[Tuple[str, str]]] = None):
        """
        Set up plugboard connections.

        Args:
            connections:
                A list of tuples of two letters to be connected on the plugboard.
                E.g. [('A', 'B')].

        """
        self.connections: Dict[str, str] = {}
        if connections is not None:
            for connection in connections:
                self.validate_connection(connection)
                letter_1, letter_2 = connection
                self.connections[letter_1] = letter_2
                self.connections[letter_2] = letter_1

    def encode(self, value: str) -> str:
        """Return encoded value for value."""
        if value in self.connections:
            return self.connections[value]
        return value

    def validate_connection(self, connection: Tuple[str, str]) -> None:
        """Raise error if connection is not valid."""
        if len(connection) != 2:
            raise InvalidPlugboard(connection)
        if connection[0] == connection[1]:
            raise InvalidPlugboard(connection)
        if connection[0] not in alphabet or connection[1] not in alphabet:
            raise InvalidPlugboard(connection)


class InvalidPlugboard(ValueError):
    """Exception for invalid plugboard setups."""

    def __init__(self, connection: Tuple[str, str]):
        """Raise exception."""
        super().__init__("{} is an invalid plugboard connection.".format(connection))
