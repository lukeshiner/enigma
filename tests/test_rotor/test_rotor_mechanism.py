"""Tests for engima's rotor mechanism."""

from enigma import Reflector, Rotor, RotorMechanism


class TestRotorMechanism:
    """Test class for enigma's rotor mechanism."""

    def get_rotors(self, settings):
        """Return rotor set."""
        return [Rotor(**setting) for setting in settings]

    def get_rotor_mechanism(
            self,
            rotors=[
                {
                    'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                    'position': 'A',
                    'ring_setting': 1,
                    'turnover_positions': ['R'],
                },
                {
                    'wiring': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
                    'position': 'A',
                    'ring_setting': 1,
                    'turnover_positions': ['F'],
                },
                {
                    'wiring': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                    'position': 'A',
                    'ring_setting': 1,
                    'turnover_positions': ['W'],
                },
            ],
            reflector=Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')):
        """Return rotor mechanism."""
        rotors = self.get_rotors(rotors)
        return RotorMechanism(rotors=rotors, reflector=reflector)

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
        assert ''.join([rotors.encode(l) for l in 'AAA']) == 'BDZ'

    def test_first_rotor_rotates(self):
        """Test that the first rotor rotates after a keypress."""
        rotors = self.get_rotor_mechanism()
        assert rotors.rotors[2].position == 'A'
        rotors.encode('A')
        assert rotors.rotors[2].position == 'B'
        rotors.encode('A')
        assert rotors.rotors[2].position == 'C'

    def test_second_rotor_rotates(self):
        """Test that the second rotor rotates."""
        rotors = self.get_rotor_mechanism()
        rotors.rotors[2].set_position('V')
        assert rotors.rotors[2].turnover_positions == ['W']
        assert rotors.rotors[1].position == 'A'
        rotors.encode('A')
        assert rotors.rotors[2].position == 'W'
        assert rotors.rotors[1].position == 'B'
