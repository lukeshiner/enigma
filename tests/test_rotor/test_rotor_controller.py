"""Tests for engima's rotor mechanism."""

from enigma import Reflector, Rotor, RotorMechanism


class TestRotorMechanism:
    """Test class for enigma's rotor mechanism."""

    def get_rotors(self, settings):
        """Return rotor set."""
        return [Rotor(**setting) for setting in settings]

    def get_rotor_mechanism(
            self,
            rotors=(
                ('EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                 'A'), ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A'),
                ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A')),
            reflector=Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')):
        """Return reflector mechanism."""
        rotors = self.get_rotors(rotors)
        return RotorMechanism(*rotors, reflector=reflector)

    def test_default_position_encoding(self):
        """
        Test the rotor mechanism returns correct.

        Input string: 'AAA'
        Rotor position 1: Rotor I
        Rotor position 2: Rotor II
        Rotor position 3: Rotor III

        All rotors in position A with ring setting of 01.
        """
        rotors = self.get_rotor_mechanism()
        assert rotors.encode('AAA') == 'BDZ'

    def test_first_rotor_rotates(self):
        """Test that the first rotor rotates after a keypress."""
        rotors = self.get_rotor_mechanism()
        assert rotors.rotors[2].position == 'A'
        rotors.encode('A')
        assert rotors.rotors[2].position == 'B'
        rotors.encode('A')
        assert rotors.rotors[2].position == 'C'
