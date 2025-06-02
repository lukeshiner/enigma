import pytest

from enigma.enigma_machine import Plugboard


@pytest.fixture
def pairs():
    return ((0, 1), (4, 6))


@pytest.fixture
def plugboard(pairs):
    return Plugboard(pairs)


def test_plugboard_has_pairs(plugboard):
    assert plugboard.pairs == {0: 1, 1: 0, 4: 6, 6: 4}


@pytest.mark.parametrize("input,output", ((0, 1), (1, 0), (4, 6), (6, 4), (2, 2)))
def test_encode(input, output, plugboard):
    assert plugboard.encode(input) == output
