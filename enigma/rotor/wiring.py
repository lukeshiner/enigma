"""The wiring class."""

from string import ascii_uppercase as alphabet


class Wiring:
    """Find pin connections for an Enima rotor."""

    def __init__(self, wiring: str):
        """
        Set wiring.

        Args:
            wiring:
                String containing the letters the pins on the right side
                will connect to for each left hand pin when the rotor is in
                position 'A'.
        """
        self.pins = [alphabet.index(char) for char in wiring]

    def __repr__(self) -> str:
        return "".join([alphabet[pin] for pin in self.pins])

    def __len__(self) -> int:
        return len(self.pins)

    def left_pin(self, right_pin: int) -> int:
        """Return the pin position on the left for one on the right."""
        return self.pins[right_pin]

    def right_pin(self, left_pin: int) -> int:
        """Return the pin position on the right for one on the left."""
        return self.pins.index(left_pin)
