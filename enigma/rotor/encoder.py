"""The Encoder class."""

from .wiring import Wiring


class Encoder:
    """Base class for encoders."""

    name = None

    def __init__(self, wiring: str):
        """Set wiring and position encodings."""
        self.wiring = Wiring(wiring)
