"""Tests for enigma's rotors."""

import pytest
from enigma import Rotor
from enigma.exceptions import InvalidRotorSetting

from .rotor_test import RotorTest


class TestRotors(RotorTest):
    """Test class for testing rotors."""

    def rotor_position_test(self, positions, ring_setting='01'):
        """Test initial position with given positions."""
        rotor = self.get_rotor()
        set_positions = []
        for position in positions:
            rotor = self.get_rotor(
                position=position, ring_setting=ring_setting)
            set_positions.append(rotor.position)
        return set_positions

    def test_straight_rotor(self):
        """Test rotor encoding does not change with straight wiring."""
        alpha = Rotor.ALPHA
        for position in alpha:
            for ring_setting in alpha:
                for reverse in (True, False):
                    rotor = Rotor(
                        wiring=alpha,
                        position=position,
                        ring_setting=ring_setting)
                    output = [
                        rotor.encode(letter, reverse=reverse)
                        for letter in alpha
                    ]
                    assert output == alpha

    def test_rotor_set_position(self):
        """Test initial position with ring setting."""
        assert self.rotor_position_test(['A', 'Q', 'Z']) == ['A', 'Q', 'Z']

    def test_rotor_set_position_with_ring_setting(self):
        """Test that rotor.set_position sets rotor position."""
        assert self.rotor_position_test(['A', 'Q', 'Z']) == ['A', 'Q', 'Z']

    def test_rotor_set_position_lower_case(self):
        """Test rotor accepts lowercase rotation settings."""
        assert self.rotor_position_test(['a', 'q', 'z']) == ['A', 'Q', 'Z']

    def test_rotor_position_numerical(self):
        """Test rotor accepts numerical rotation settings."""
        self.rotor_position_test([1, 17, 26]) == ['A', 'Q', 'Z']

    def test_rotor_position_numeric_string(self):
        """Test rotor accepts numerical rotation settings."""
        self.rotor_position_test(['01', '17', '26']) == ['A', 'Q', 'Z']

    def test_rotor_position_raises_with_invalid_setting(self):
        """Test exception is raised with invalid rotor settings."""
        with pytest.raises(InvalidRotorSetting):
            self.rotor_position_test([85])
        with pytest.raises(InvalidRotorSetting):
            self.rotor_position_test(['38'])
        with pytest.raises(InvalidRotorSetting):
            self.rotor_position_test(['*'])
        with pytest.raises(InvalidRotorSetting):
            self.rotor_position_test(['ABC'])

    def test_rotor_starting_position(self):
        """Test rotors starting position is correct for passed argument."""
        assert self.get_rotor(position='A').position == 'A'
        assert self.get_rotor(position='b').position == 'B'
        assert self.get_rotor(position=1).position == 'A'
        assert self.get_rotor(position=3).position == 'C'
        assert self.get_rotor(position='05').position == 'E'
        assert self.get_rotor(position='A', ring_setting='02').position == 'A'
        assert self.get_rotor(position='C', ring_setting='02').position == 'C'
        assert self.get_rotor(position=26, ring_setting='02').position == 'Z'

    def test_rotor_complete_rotation(self):
        """Test that a rotor can complete a full rotation."""
        rotor = self.get_rotor(ring_setting='02')
        initial_position = rotor.position
        for position in range(len(rotor.wiring)):
            rotor.rotate()
        assert initial_position == rotor.position

    def test_rotor_position_updates_on_rotation(self):
        """Test rotor position is correct after rotation."""
        rotor = self.get_rotor()
        assert rotor.position == 'A'
        rotor.rotate()
        assert rotor.position == 'B'
        rotor.rotate()
        assert rotor.position == 'C'
        rotor = self.get_rotor()
        rotor.rotate(turns=3)
        assert rotor.position == 'D'

    def test_get_ring_setting(self):
        """Test rotor sets and reports ring setting correctly."""
        rotor = self.get_rotor(ring_setting='02')
        assert rotor.ring_setting == '02'

    def test_ring_setting(self):
        """Test rotor encoding with ring setting."""
        rotor = self.get_rotor(ring_setting='02')
        assert rotor.encode('A') == 'K'
        assert rotor.encode('Q') == 'I'
        assert rotor.encode('H') == 'E'
        rotor.rotate()
        assert rotor.encode('A') == 'E'

    def test_rotor_I_position_A_input_A(self):
        """Test rotor encoding right to left without rotation."""
        rotor = self.get_rotor()
        assert rotor.encode('A') == 'E'

    def test_rotor_I_position_A_after_rotation(self):
        """Test rotor encoding right to left with a single rotation."""
        rotor = self.get_rotor()
        rotor.rotate()
        assert rotor.encode('A') == 'J'
        assert rotor.encode('Q') == 'T'
        assert rotor.encode('H') == 'U'

    def test_rotor_III(self):
        """Test rotor encoding right to left with multiple rotations."""
        rotor = self.get_rotor(
            wiring='BDFHJLCPRTXVZNYEIWGAKMUSQO', position='D')
        assert rotor.encode('A') == 'E'
        assert rotor.encode('Q') == 'X'
        assert rotor.encode('H') == 'U'

    def test_rotor_I_position_A_input_A_reverse(self):
        """Test rotor encoding left to right without rotation."""
        rotor = self.get_rotor(
            wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', position='A')
        assert rotor.encode('A', reverse=True) == 'U'

    def test_rotor_I_position_A_after_rotation_reverse(self):
        """Test rotor encoding left to right with a single rotation."""
        rotor = self.get_rotor(
            wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', position='A')
        rotor.rotate()
        assert rotor.encode('A', reverse=True) == 'V'
        assert rotor.encode('Q', reverse=True) == 'W'
        assert rotor.encode('H', reverse=True) == 'U'

    def test_rotor_III_reverse(self):
        """Test rotor encoding left to right with multiple rotations."""
        rotor = self.get_rotor(
            wiring='BDFHJLCPRTXVZNYEIWGAKMUSQO', position='D')
        assert rotor.encode('A', reverse=True) == 'Y'
        assert rotor.encode('Q', reverse=True) == 'G'
        assert rotor.encode('H', reverse=True) == 'R'
