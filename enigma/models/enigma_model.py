"""Base classes for specific models of Enigma machine."""

from enigma import Enigma, Plugboard, Reflector, Rotor


class PresetRotor(Rotor):
    """Base class for preset rotors."""

    def __init__(self, position, ring_setting):
        """
        Set up rotor.

        Kwargs:
            ring_setting:
                The offset of the letters on the rotor as a letter or number.
                Default: 'A'.

            position:
                The starting position of the rotor as a letter or number.
                Default: 'A'.
        """
        super().__init__(
            wiring=self.wiring,
            turnover_positions=self.turnover_positions,
            position=position,
            ring_setting=ring_setting)


class PresetReflector(Reflector):
    """Base class for preset reflectors."""

    def __init__(self):
        """Set up reflector."""
        super().__init__(wiring=self.wiring)


class EnigmaModel(Enigma):
    """Base class for enigma models."""

    ROTORS = 'rotors'
    POSITIONS = 'positions'
    RING_SETTINGS = 'ring_settings'
    REFLECTOR = 'reflector'
    PLUGBOARD_PAIRS = 'plugboard_pairs'

    rotors = []
    reflectors = []

    def __init__(self, **kwargs):
        """
        Set up Enigma object.

        Kwargs:
            rotors:
                Iterable containing the names of the rotors to use.
                E.g. ('I', 'II', 'III').
            positions:
                str or iterable containng the initial letter positions of the
                rotors. E.g. 'AAA'.
            ring_settings:
                Iterable containing the ring settings of the rotors as str or
                int. E.g ('01', '01', '01')
            plugboard_pairs:
                Iterable containing two character strings of letter pairs for
                the plugboard. E.g. ['AB', 'QZ']
            reflector:
                Name of the reflector to use.
        """
        self.initial_settings = kwargs
        self.set_initial_settings()

    def set_initial_settings(self):
        """Reset Enigma to it's initial settings."""
        positions = self.initial_settings[self.POSITIONS]
        ring_settings = self.initial_settings[self.RING_SETTINGS]
        reflector = self.reflectors[self.initial_settings[self.REFLECTOR]]()
        plugboard_pairs = self.initial_settings[self.PLUGBOARD_PAIRS]
        rotors = []
        for i in range(3):
            rotor_class = self.rotors[self.initial_settings[self.ROTORS][i]]
            rotor = rotor_class(
                position=positions[i], ring_setting=int(ring_settings[i]))
            rotors.append(rotor)
        plugboard = Plugboard(plugboard_pairs)
        super().__init__(
            rotors=rotors, reflector=reflector, plugboard=plugboard)
