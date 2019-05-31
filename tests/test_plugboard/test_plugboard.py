"""Tests for Engma's plugboard."""

import unittest

from enigma import Plugboard
from enigma.exceptions import InvalidPlugboard


class TestPlugboard(unittest.TestCase):
    """Tests for Enigma's plugboard."""

    def test_empty_plugboard(self):
        """Test empty plugboard does not change encoding."""
        board = Plugboard([])
        self.assertEqual(board.encode("A"), "A")
        self.assertEqual(board.encode("Q"), "Q")

    def test_plugboard_encoding(self):
        """Test that the plugboard can encode values."""
        board = Plugboard([("A", "Q"), ("N", "V")])
        self.assertEqual(board.encode("A"), "Q")
        self.assertEqual(board.encode("Q"), "A")
        self.assertEqual(board.encode("N"), "V")
        self.assertEqual(board.encode("V"), "N")
        self.assertEqual(board.encode("L"), "L")

    def test_plugboard_raises_for_invalid_connection(self):
        """Test a plugboard cannot be created with an invalid setup."""
        with self.assertRaises(InvalidPlugboard):
            Plugboard([("A", "A")])

    def test_plugboard_raises_for_invalid_argument(self):
        """Test a plugboard raises for a connection has the wrong number of arguments."""
        with self.assertRaises(InvalidPlugboard):
            Plugboard([("A")])
        with self.assertRaises(InvalidPlugboard):
            Plugboard([("A", "B", "C")])
        with self.assertRaises(InvalidPlugboard):
            Plugboard([("@", "B")])
