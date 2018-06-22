"""Tests for Engma's plugboard."""

import pytest
from enigma import Plugboard
from enigma.exceptions import InvalidPlugboard


def test_empty_plugboard():
    """Test empty plugboard does not change encoding."""
    board = Plugboard([])
    assert board.encode('A') == 'A'
    assert board.encode('Q') == 'Q'


def test_plugboard_encoding():
    """Test that the plugboard can encode values."""
    board = Plugboard([('A', 'Q'), ('N', 'V')])
    assert board.encode('A') == 'Q'
    assert board.encode('Q') == 'A'
    assert board.encode('N') == 'V'
    assert board.encode('V') == 'N'
    assert board.encode('L') == 'L'


def test_invalid_plugboard_raises():
    """Test a plugboard cannot be created with an invalid setup."""
    with pytest.raises(InvalidPlugboard):
        Plugboard([('A', 'A')])
