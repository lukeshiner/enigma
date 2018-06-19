"""Tests for enigma.rotor.wiring.Wiring."""

from enigma.rotor.wiring import Wiring

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_wiring_pins():
    """Test Wiring can be instanicated."""
    wiring = Wiring(ALPHA)
    output = [wiring.left_pin(i) for i in range(len(ALPHA))]
    assert output == list(range(len(ALPHA)))


def test_wiring_to_sting():
    """Test Wiring classes __repr__ method."""
    wiring = Wiring(ALPHA)
    assert str(wiring) == ALPHA
