"""Enigma."""

from string import ascii_uppercase


class Reflector:
    """Class representing Enigma reflectors."""

    def __init__(self, wiring):
        """
        The Reflector class.

        Simulates an Enigma reflector.

        Args:
            wiring list(int): A list of output pins ordered by input pin.
        """
        self.wiring = wiring

    def connection(self, pin):
        """Return the pin connected to pin position pin."""
        return self.wiring[pin]

    def wiring_string(self):
        """Return the rotor's wiring as a string."""
        return "".join([ascii_uppercase[char] for char in self.wiring])

    def __repr__(self):
        return f"<Reflector: {self.wiring_string()}>"


class Rotor:
    """Class representing Enigma rotors."""

    def __init__(self, wiring, notches, ring_position=0):
        """
        The Rotor class.

        Simulates an Enigma rotor.

        Args:
            wiring (list(int)): A list of output pins ordered by input pin.
            notches (list(int)): A list of notch positions.
        """
        self.wiring = wiring
        self.notches = set(notches)
        self.ring_position = ring_position
        self.rotational_position = 0

    def right_to_left(self, pin_position):
        """Return the output pin position for an input pin."""
        pin_number = self._position_to_wire(pin_position)
        return self._wire_to_position(self.wiring[pin_number])

    def left_to_right(self, pin_position):
        """Return the input pin for an output pin."""
        pin_number = self._position_to_wire(pin_position)
        return self._wire_to_position(self.wiring.index(pin_number))

    def rotate(self):
        """Increase rotation position."""
        self.rotational_position = (self.rotational_position + 1) % 26

    def wiring_string(self):
        """Return the rotor's wiring as a string."""
        return "".join([ascii_uppercase[char] for char in self.wiring])

    def notches_string(self):
        """Return the rotor's notches as a string."""
        return "".join([ascii_uppercase[char] for char in self.notches])

    def ring_setting_string(self):
        """Return the rotor's ring setting as a string."""
        return str(self.ring_position + 1)

    def position_string(self):
        """Return the rotor's current position as a string."""
        return ascii_uppercase[self.rotational_position]

    def _position_to_wire(self, input_pin):
        wire_input = input_pin + self.rotational_position
        return (wire_input - self.ring_position) % 26

    def _wire_to_position(self, wire_position):
        return ((wire_position + self.ring_position) - self.rotational_position) % 26

    def __repr__(self):
        return (
            f"<Rotor: {self.wiring_string()} - {self.notches_string()} - "
            f"{self.ring_setting_string()} - {self.position_string()}>"
        )


class RotorMechanism:
    """Class representing Enigma rotor mechanisms."""

    def __init__(self, rotors=None, reflector=None):
        """
        The Rotor class.

        Simulates an Enigma rotor.

        Args:
            rotors (list(Rotor)): A list of rotors used, from right to left.
            reflector (Reflector): The reflector used.
        """
        self.rotors = rotors or []
        self.reflector = reflector or []

    def encode(self, input):
        """Return the output pin for input pin input."""
        for rotor in reversed(self.rotors):
            input = rotor.right_to_left(input)
        input = self.reflector.connection(input)
        for rotor in self.rotors:
            input = rotor.left_to_right(input)
        return input

    def update_rotor_positions(self):
        """Update the rotor positions."""
        self.rotors[-1].rotate()
        for i in range(-2, -len(self.rotors) - 1, -1):
            if self.rotors[i + 1].rotational_position in self.rotors[i + 1].notches:
                self.rotors[i].rotate()
            else:
                return

    def set_positions(self, positions):
        """Set the positions of the rotors."""
        for i, position in enumerate(positions):
            self.rotors[i].rotational_position = position

    def set_ring_settings(self, ring_settings):
        """Set the rotor's ring settings."""
        for i, rotor in enumerate(self.rotors):
            rotor.ring_position = ring_settings[i]


class Plugboard:
    """Class representing an Engima plugboard."""

    def __init__(self, pairs=None):
        """
        The Plugboard class.

        Simulates an Enigma plugboard.

        Args:
            pairs (tupe(tuple(int,int))): A tuple of plugboard connection pairs.
        """
        self.set_pairs(pairs or ())

    def set_pairs(self, pairs):
        """Set the plugboard wiring."""
        self.pairs = {}
        for pair in pairs:
            self.pairs[pair[0]] = pair[1]
            self.pairs[pair[1]] = pair[0]

    def encode(self, input):
        """Return the plugboard output for an input."""
        return self.pairs.get(input, input)


class EnigmaMachine:
    """Class representing and Enigma machine."""

    rotor_mechanism_class = RotorMechanism
    plugboard_class = Plugboard

    def __init__(self):
        """Class representing and Enigma machine."""
        self.rotor_mechanism = self.rotor_mechanism_class()
        self.plugboard = self.plugboard_class()

    def encode(self, string, block_size=0):
        """Return an encoded string."""
        plain_text = self._string_to_ints(string)
        cipher_text_ints = [self._int_encode(char) for char in plain_text]
        cipher_text = self._ints_to_string(cipher_text_ints)
        return self.to_blocks(text=cipher_text, block_size=block_size)

    @staticmethod
    def to_blocks(text, block_size):
        """Return text with spaces every block_size characters."""
        if block_size == 0:
            return text
        blocks = []
        for i in range(0, len(text), block_size):
            blocks.append("".join(text[i : i + block_size]))
        return " ".join(blocks)

    def set_rotors(self, rotors):
        """
        Change the machine's installed rotors.

        Args:
            rotors (list(Rotor)): A list of rotor instances.
        """
        self.rotor_mechanism.rotors = rotors

    def set_ring_settings(self, ring_settings):
        """
        Set the installed rotor's ring settings.

        Args:
            ring_settings (list(int)): A list of the new ring settings for each
                rotor from left to right. The setting is a zero-based integer
                offset where 0 is equivalent to the default A position.
        """
        self.rotor_mechanism.set_ring_settings(ring_settings)

    def set_reflector(self, reflector):
        """
        Set the machine's installed reflector.

        Args:
            reflector (Reflector): The Reflector instance to use.
        """
        self.rotor_mechanism.reflector = reflector

    def set_rotor_positions(self, positions):
        """
        Set the position of the rotors.

        Args:
            positions (list(int)): The new positions of the rotors as a list of
                integers ordered from the left-most rotor to the right-most. The
                setting is a zero based offset so a setting of 0 is equvalent to
                the A position.
        """
        self.rotor_mechanism.set_positions(positions)

    def set_plugboard(self, plugboard_pairs):
        """
        Set the plugboard pairs.

        Args:
            plugboard_pairs (tuple(tuple(int,int))): A tuple containing tuples
                of two integers where each pair represents a plugboard
                connection. The integers are zero-based so a 0 indicates a
                connection to A, 25 to Z.
        """
        self.plugboard.set_pairs(plugboard_pairs)

    def _int_encode(self, input):
        self.rotor_mechanism.update_rotor_positions()
        return self._encode_key(input)

    def _encode_key(self, key_number):
        return self.plugboard.encode(
            self.rotor_mechanism.encode(self.plugboard.encode(key_number))
        )

    def _string_to_ints(self, string):
        return [
            ascii_uppercase.index(char.upper()) for char in string if char.isalpha()
        ]

    def _ints_to_string(self, ints):
        return "".join((ascii_uppercase[i] for i in ints))
