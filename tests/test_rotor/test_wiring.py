"""Tests for enigma.rotor.wiring.Wiring class."""

import unittest

from enigma.rotor.wiring import Wiring

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class TestWiring(unittest.TestCase):
    """Tests for enigma.rotor.wiring.Wiring class."""

    def test_wiring_pins(self):
        """Test Wiring can be instanicated."""
        wiring = Wiring(ALPHA)
        output = [wiring.left_pin(i) for i in range(len(ALPHA))]
        self.assertEqual(output, list(range(len(ALPHA))))

    def test_wiring_to_string(self):
        """Test Wiring classes __repr__ method."""
        wiring = Wiring(ALPHA)
        self.assertEqual(str(wiring), ALPHA)
