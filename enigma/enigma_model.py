"""Enigma."""

from string import ascii_uppercase

from . import rotors
from .enigma_machine import EnigmaMachine


class EnigmaModel(EnigmaMachine):
    """Enigma machine."""

    def setup(
        self, rotors, reflector, ring_settings, plugboard_pairs, starting_positions
    ):
        """Set up the Enigma machine."""
        self.set_rotors(rotors)
        self.set_reflector(reflector)
        self.set_ring_settings(ring_settings)
        self.set_rotor_positions(starting_positions)
        self.set_plugboard(plugboard_pairs)

    def set_reflector(self, reflector_name):
        """Set the reflector type."""
        reflector = self.available_reflectors[reflector_name]()
        super().set_reflector(reflector)

    def set_rotors(self, rotor_names):
        """Set the used rotors and ring settings."""
        rotor_names = rotor_names.split(" ")
        rotors = [self.available_rotors[name]() for name in rotor_names]
        super().set_rotors(rotors)

    def set_ring_settings(self, ring_settings):
        """Set the rotor ring settings."""
        if ring_settings:
            ring_settings = [int(setting) - 1 for setting in ring_settings.split()]
        else:
            ring_settings = [0 for _ in range(self.rotor_count)]
        super().set_ring_settings(ring_settings)

    def set_rotor_positions(self, positions):
        """Set the rotor positions."""
        super().set_rotor_positions(
            [ascii_uppercase.index(char.upper()) for char in positions]
        )

    def set_plugboard(self, plugboard_pairs):
        """Set the plugboard."""
        plug_pairs = plugboard_pairs.split(" ")
        plugboard_pairs = []
        for plug_pair in plug_pairs:
            plugboard_pairs.append(
                tuple([ascii_uppercase.index(char) for char in plug_pair])
            )
        super().set_plugboard(tuple(plugboard_pairs))


class EnigmaI(EnigmaModel):
    """Enigma model I."""

    available_rotors = {
        "I": rotors.rotor_I,
        "II": rotors.rotor_II,
        "III": rotors.rotor_III,
    }
    available_reflectors = {"A": rotors.reflector_A}
    rotor_count = 3

    def setup(self, rotors, ring_settings, plugboard_pairs, starting_positions):
        """Set up the Enigma machine."""
        super().setup(
            rotors=rotors,
            ring_settings=ring_settings,
            plugboard_pairs=plugboard_pairs,
            starting_positions=starting_positions,
            reflector="A",
        )


class EnigmaM3(EnigmaModel):
    """Enigma model M3."""

    available_rotors = {
        "I": rotors.rotor_I,
        "II": rotors.rotor_II,
        "III": rotors.rotor_III,
        "IV": rotors.rotor_IV,
        "V": rotors.rotor_V,
        "VI": rotors.rotor_VI,
        "VII": rotors.rotor_VII,
        "VIII": rotors.rotor_VIII,
    }
    available_reflectors = {
        "A": rotors.reflector_A,
        "B": rotors.reflector_B,
        "C": rotors.reflector_C,
    }
    rotor_count = 3
