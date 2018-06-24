"""Tests for enigma.rotor.encoder.Encoder."""

import unittest

from enigma.rotor.encoder import Encoder


class TestEncoder(unittest.TestCase):
    """Test for the Encoder class."""

    def test_encoder(self):
        """Test encoder can be instanicated."""
        Encoder(Encoder.ALPHA)
