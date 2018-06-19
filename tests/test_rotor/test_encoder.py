"""Tests for enigma.rotor.encoder.Encoder."""

from enigma.rotor.encoder import Encoder


def test_encoder():
    """Test encoder can be instanicated."""
    Encoder(Encoder.ALPHA)
