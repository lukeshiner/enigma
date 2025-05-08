"""Base classes for specific models of Enigma machine."""

from __future__ import annotations

from typing import Optional, Sequence, Tuple

from enigma import Enigma, Plugboard, Reflector, Rotor


class EnigmaModel:
    """Base class for enigma models."""

    ROTORS = "rotors"
    POSITIONS = "positions"
    RING_SETTINGS = "ring_settings"
    REFLECTOR = "reflector"
    PLUGBOARD_PAIRS = "plugboard_pairs"

    name: str

    available_rotors: dict[str, Rotor]
    available_reflectors: dict[str, Reflector]

    rotors: Sequence[Rotor] = []
    reflectors: Sequence[Reflector] = []
    rotor_count: int

    @classmethod
    def from_strings(
        cls,
        rotors: str,
        reflector: str,
        plugboard: str,
        positions: Optional[str] = None,
        ring_settings: Optional[Sequence[int]] = None,
    ) -> Enigma:
        """Return an Enigma instance."""
        rotors_ = [cls.available_rotors[_.upper()] for _ in rotors.split(" ")]
        reflector_ = cls.available_reflectors[reflector.upper()]
        plugboard_ = Plugboard(cls._read_plugboard_string(plugboard))
        if ring_settings is not None:
            for i, rotor in enumerate(rotors_):
                rotor.ring_setting = ring_settings[i]
        if positions is not None:
            for i, rotor in enumerate(rotors_):
                rotor.set_start_position(positions[i])
        return Enigma(rotors=rotors_, reflector=reflector_, plugboard=plugboard_)

    @classmethod
    def _read_plugboard_string(cls, plugboard_string: str) -> list[Tuple[str, str]]:
        plugboard_settings: list[Tuple[str, str]] = []
        for letter_pair in plugboard_string.split(" "):
            plugboard_settings.append((letter_pair[0], letter_pair[1]))
        return plugboard_settings
