"""Tests for enigma.rotor.encoder.Encoder."""

import unittest
from string import ascii_uppercase

from enigma.rotor.encoder import Encoder


class TestEncoder(unittest.TestCase):
    """Test for the Encoder class."""

    def test_encoder(self):
        """Test encoder can be instanicated."""
        Encoder(ascii_uppercase)
