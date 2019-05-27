"""Base classes for specific models of Enigma machine."""

from typing import Dict, Sequence, Type

from enigma import Enigma, Plugboard, Reflector, Rotor


class PresetRotor(Rotor):
    """Base class for preset rotors."""

    set_wiring: str
    turnover_positions: Sequence[str]

    def __init__(self, position: str, ring_setting: int):
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
            wiring=self.set_wiring,
            turnover_positions=self.turnover_positions,
            position=position,
            ring_setting=ring_setting,
        )


class PresetReflector(Reflector):
    """Base class for preset reflectors."""

    set_wiring: str

    def __init__(self) -> None:
        """Set up reflector."""
        super().__init__(wiring=self.set_wiring)


class EnigmaModel(Enigma):
    """Base class for enigma models."""

    ROTORS = "rotors"
    POSITIONS = "positions"
    RING_SETTINGS = "ring_settings"
    REFLECTOR = "reflector"
    PLUGBOARD_PAIRS = "plugboard_pairs"

    available_rotors: Dict[str, Type[PresetRotor]]
    available_reflectors: Dict[str, Type[PresetReflector]]

    rotors: Sequence[Rotor] = []
    reflectors: Sequence[Reflector] = []

    def __init__(
        self,
        *,
        rotors: Sequence[str],
        positions: Sequence[str],
        ring_settings: Sequence[str],
        plugboard_pairs: Sequence[str],
        reflector: str
    ):
        """
        Set up Enigma object.

        Kwargs:
            rotors:
                Iterable containing the names of the rotors to use.
                E.g. ('I', 'II', 'III').
            positions:
                Iterable containng the initial letter positions of the
                rotors. E.g. 'AAA'.
            ring_settings:
                Iterable containing the ring settings of the rotors as str.
                E.g ('01', '01', '01')
            plugboard_pairs:
                Iterable containing two character strings of letter pairs for
                the plugboard. E.g. ['AB', 'QZ']
            reflector:
                Name of the reflector to use.
        """
        positions = positions
        ring_settings = ring_settings
        used_reflector = self.available_reflectors[reflector]()
        plugboard_pairs = plugboard_pairs
        used_rotors = []
        for i in range(3):
            rotor_class = self.available_rotors[rotors[i]]
            rotor = rotor_class(
                position=positions[i], ring_setting=int(ring_settings[i])
            )
            used_rotors.append(rotor)
        plugboard = Plugboard(plugboard_pairs)
        super().__init__(
            rotors=used_rotors, reflector=used_reflector, plugboard=plugboard
        )
