"""Tests for the engima's reflectors."""

import unittest

from enigma import Reflector


class TestReflector(unittest.TestCase):
    """Test class for testing reflectors."""

    def test_reflector_output(self):
        """Test refelectors give a correct encoding."""
        reflector = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.assertEqual(reflector.encode("A"), "Y")
        self.assertEqual(reflector.encode("Q"), "E")
        self.assertEqual(reflector.encode("H"), "D")
