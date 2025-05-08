"""Tests for Enigma models."""

import unittest

from enigma.models import M3


class TestM3(unittest.TestCase):
    """Tests for the M3 model Enigma machine."""

    def test_M3(self):
        """Test message encoding with Enigma model M3."""
        message = (
            "EDPUD NRGYS ZRCXN UYTPO MRMBO FKTBZ REZKM LXLVE FGUEY SIOZV"
            "EQMIK UBPMM YLKLT TDEIS MDICA GYKUA CTCDO MOHWX MUUIA UBSTS LRNBZ"
            "SZWNR FXWFY SSXJZ VIJHI DISHP RKLKA YUPAD TXQSP INQMA TLPIF SVKDA"
            "SCTAC DPBOP VHJK"
        )
        enigma = M3.from_strings(
            rotors="II IV V",
            positions="BLA",
            ring_settings=(2, 21, 12),
            reflector="B",
            plugboard="AV BS CG DL FU HZ IN KM OW RX",
        )
        expected_output = (
            "AUFKL XABTE ILUNG XVONX KURTI NOWAX KURTI NOWAX NORDW ESTLX "
            "SEBEZ XSEBE ZXUAF FLIEG ERSTR ASZER IQTUN GXDUB ROWKI XDUBR "
            "OWKIX OPOTS CHKAX OPOTS CHKAX UMXEI NSAQT DREIN ULLXU HRANG "
            "ETRET ENXAN GRIFF XINFX RGTX"
        )
        output = enigma.encode(message, blocks=5)
        self.assertEqual(output, expected_output)
