"""Exceptions for enigma."""


class InvalidPlugboard(ValueError):
    """Exception for invalid plugboard setups."""

    def __init__(self, connection: tuple[str, str]):
        """Raise exception."""
        super().__init__("{} is an invalid plugboard connection.".format(connection))
