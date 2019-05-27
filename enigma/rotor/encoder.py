"""The Encoder class."""

from .wiring import Wiring


class Encoder:
    """Base class for encoders."""

    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    name = None

    def __init__(self, wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT"):
        """Set wiring and position encodings."""
        self.wiring = Wiring(wiring)
