"""Tests for the engima's reflectors."""

import unittest

from enigma import Reflector


class TestReflector(unittest.TestCase):
    """Test class for testing reflectors."""

    def test_reflector_output(self):
        """Test refelectors give a correct encoding."""
        rotor = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.assertEqual(rotor.encode("A"), "Y")
        self.assertEqual(rotor.encode("Q"), "E")
        self.assertEqual(rotor.encode("H"), "D")
