"""Exceptions for enigma.rotor."""


class InvalidRotorSetting(ValueError):
    """Exception for invalid rotor settings."""

    def __init__(self, setting: str):
        """Raise Value Error."""
        super().__init__("'{}' is not a valid rotor setting".format(setting))
