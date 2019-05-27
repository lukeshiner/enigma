"""Tests for enigma's rotors."""

from string import ascii_uppercase

from enigma import Rotor

from .rotor_test import RotorTest


class TestRotors(RotorTest):
    """Test class for testing rotors."""

    def rotor_position_test(self, positions, ring_setting=1):
        """Test initial position with given positions."""
        rotor = self.get_rotor()
        set_positions = []
        for position in positions:
            rotor = self.get_rotor(position=position, ring_setting=ring_setting)
            set_positions.append(rotor.position)
        return set_positions

    def rotor_turnover_positions_test(self, turnover_positionses, ring_setting=1):
        """Test initial position with given positions."""
        rotor = self.get_rotor()
        set_notches = []
        for turnover_positions in turnover_positionses:
            rotor = self.get_rotor(
                turnover_positions=turnover_positions, ring_setting=ring_setting
            )
            set_notches.append(rotor.turnover_positions)
        return set_notches

    def test_straight_rotor(self):
        """Test rotor encoding does not change with straight wiring."""
        for position in ascii_uppercase:
            for ring_setting in range(1, len(ascii_uppercase) + 1):
                for reverse in (True, False):
                    rotor = Rotor(
                        wiring=ascii_uppercase,
                        position=position,
                        ring_setting=ring_setting,
                    )
                    output = [
                        rotor.encode(letter, reverse=reverse)
                        for letter in ascii_uppercase
                    ]
                    self.assertEqual(output, list(ascii_uppercase))

    def test_set_rotor_position(self):
        """Test initial position with ring setting."""
        self.assertEqual(self.rotor_position_test(["A", "Q", "Z"]), ["A", "Q", "Z"])

    def test_set_rotor_position_with_ring_setting(self):
        """Test that rotor.set_position sets rotor position."""
        self.assertEqual(self.rotor_position_test(["A", "Q", "Z"]), ["A", "Q", "Z"])

    def test_set_rotor_turnover_positions(self):
        """Test initial turnover positions with ring setting."""
        self.assertEqual(
            self.rotor_turnover_positions_test([["A"], ["Q"], ["Z"]]),
            [["A"], ["Q"], ["Z"]],
        )

    def test_set_multiple_rotor_turnover_positions(self):
        """Test rotor accepts a list of turnover position settings."""
        self.assertEqual(self.rotor_turnover_positions_test(["A", "Q"]), ["A", "Q"])

    def test_rotor_starting_position(self):
        """Test rotors starting position is correct for passed argument."""
        self.assertEqual(self.get_rotor(position="A").position, "A")
        self.assertEqual(self.get_rotor(position="Q").position, "Q")

    def test_rotor_complete_rotation(self):
        """Test that a rotor can complete a full rotation."""
        rotor = self.get_rotor(ring_setting=2)
        initial_position = rotor.position
        for position in range(len(rotor.wiring)):
            rotor.rotate()
        self.assertEqual(initial_position, rotor.position)

    def test_rotor_position_updates_on_rotation(self):
        """Test rotor position is correct after rotation."""
        rotor = self.get_rotor()
        self.assertEqual(rotor.position, "A")
        rotor.rotate()
        self.assertEqual(rotor.position, "B")
        rotor.rotate()
        self.assertEqual(rotor.position, "C")
        rotor = self.get_rotor()
        rotor.rotate(turns=3)
        self.assertEqual(rotor.position, "D")

    def test_get_ring_setting(self):
        """Test rotor sets and reports ring setting correctly."""
        rotor = self.get_rotor(ring_setting=2)
        self.assertEqual(rotor.ring_setting, 2)

    def test_ring_setting(self):
        """Test rotor encoding with ring setting."""
        rotor = self.get_rotor(ring_setting=2)
        self.assertEqual(rotor.encode("A"), "K")
        self.assertEqual(rotor.encode("Q"), "I")
        self.assertEqual(rotor.encode("H"), "E")
        rotor.rotate()
        self.assertEqual(rotor.encode("A"), "E")

    def test_rotor_rotate_next_rotor(self):
        """Test rotor.get_next_rotor works correctly."""
        rotor = self.get_rotor(position="A", turnover_positions=["C"])
        self.assertFalse(rotor.rotate_next_rotor())
        rotor.rotate()
        self.assertFalse(rotor.rotate_next_rotor())
        rotor.rotate()
        self.assertEqual(rotor.position, "C")
        self.assertEqual(rotor.turnover_positions, ["C"])
        self.assertTrue(rotor.rotate_next_rotor())

    def test_rotor_I_position_A_input_A(self):
        """Test rotor encoding right to left without rotation."""
        rotor = self.get_rotor()
        self.assertEqual(rotor.encode("A"), "E")

    def test_rotor_I_position_A_after_rotation(self):
        """Test rotor encoding right to left with a single rotation."""
        rotor = self.get_rotor()
        rotor.rotate()
        self.assertEqual(rotor.encode("A"), "J")
        self.assertEqual(rotor.encode("Q"), "T")
        self.assertEqual(rotor.encode("H"), "U")

    def test_rotor_III(self):
        """Test rotor encoding right to left with multiple rotations."""
        rotor = self.get_rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", position="D")
        self.assertEqual(rotor.encode("A"), "E")
        self.assertEqual(rotor.encode("Q"), "X")
        self.assertEqual(rotor.encode("H"), "U")

    def test_rotor_I_position_A_input_A_reverse(self):
        """Test rotor encoding left to right without rotation."""
        rotor = self.get_rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", position="A")
        self.assertEqual(rotor.encode("A", reverse=True), "U")

    def test_rotor_I_position_A_after_rotation_reverse(self):
        """Test rotor encoding left to right with a single rotation."""
        rotor = self.get_rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", position="A")
        rotor.rotate()
        self.assertEqual(rotor.encode("A", reverse=True), "V")
        self.assertEqual(rotor.encode("Q", reverse=True), "W")
        self.assertEqual(rotor.encode("H", reverse=True), "U")

    def test_rotor_III_reverse(self):
        """Test rotor encoding left to right with multiple rotations."""
        rotor = self.get_rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", position="D")
        self.assertEqual(rotor.encode("A", reverse=True), "Y")
        self.assertEqual(rotor.encode("Q", reverse=True), "G")
        self.assertEqual(rotor.encode("H", reverse=True), "R")
