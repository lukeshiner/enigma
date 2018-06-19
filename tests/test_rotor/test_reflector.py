"""Tests for the engima's reflectors."""

from enigma import Reflector


class TestReflector:
    """Test class for testing reflectors."""

    def test_reflector_output(self):
        """Test refelectors give a correct encoding."""
        rotor = Reflector(wiring='YRUHQSLDPXNGOKMIEBFZCWVJAT')
        assert rotor.encode('A') == 'Y'
        assert rotor.encode('Q') == 'E'
        assert rotor.encode('H') == 'D'
