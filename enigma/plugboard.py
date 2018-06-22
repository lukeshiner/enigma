"""Enigma's Plugboard."""


class Plugboard:
    """Enigma's Plugboard."""

    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, connections=[]):
        """
        Set up plugboard connections.

        Args:
            connections:
                A list of pairs of letters to be connected on the plugboard.
                E.g. [('A', 'B')].

        """
        self.connections = {}
        for connection in connections:
            self.validate_connection(connection)
            letter_1, letter_2 = connection
            self.connections[letter_1] = letter_2
            self.connections[letter_2] = letter_1

    def encode(self, value):
        """Return encoded value for value."""
        if value in self.connections:
            return self.connections[value]
        return value

    def validate_connection(self, connection):
        """Raise error if connection is not valid."""
        if len(connection) != 2:
            raise InvalidPlugboard(connection)
        if connection[0] == connection[1]:
            raise InvalidPlugboard(connection)
        if connection[0] not in self.ALPHA or connection[1] not in self.ALPHA:
            raise InvalidPlugboard(connection)


class InvalidPlugboard(ValueError):
    """Exception for invalid plugboard setups."""

    def __init__(self, connection):
        """Raise exception."""
        super().__init__(
            '{} is an invalid plugboard connection.'.format(connection))
