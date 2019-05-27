"""The wiring class."""


class Wiring:
    """Find pin connections for an Enima rotor."""

    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, wiring):
        """
        Set wiring.

        Args:
            wiring:
                String containing the letters the pins on the right side
                will connect to for each left hand pin when the rotor is in
                position 'A'.
        """
        self.pins = [self.ALPHA.index(char) for char in wiring]

    def __repr__(self):
        return "".join([self.ALPHA[pin] for pin in self.pins])

    def __len__(self):
        return len(self.pins)

    def left_pin(self, right_pin):
        """Return the pin position on the left for one on the right."""
        return self.pins[right_pin]

    def right_pin(self, left_pin):
        """Return the pin position on the right for one on the left."""
        return self.pins.index(left_pin)
