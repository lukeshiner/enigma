import pytest

from enigma.enigma_model import EnigmaI, EnigmaM3


@pytest.fixture
def enigma_test():
    def _enigma_test(
        enigma_model,
        enigma_settings,
        input_text,
        output_text,
    ):
        enigma = enigma_model()
        enigma.setup(**enigma_settings)
        assert enigma.encode(input_text) == output_text.replace(" ", "")

    return _enigma_test


@pytest.mark.integration_test
def test_enimga_1_with_message_from_instruction_manual(enigma_test):
    input_text = "GCDSE AHUGW TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ"
    output_text = "FEIND LIQEI NFANT ERIEK OLONN EBEOB AQTET XANFA NGSUE DAUSG ANGBA ERWAL DEXEN DEDRE IKMOS TWAER TSNEU STADT"
    enigma_settings = {
        "rotors": "II I III",
        "ring_settings": "24 13 22",
        "plugboard_pairs": "AM FI NV PS TU WZ",
        "starting_positions": "ABL",
    }
    enigma_test(
        enigma_model=EnigmaI,
        enigma_settings=enigma_settings,
        input_text=input_text,
        output_text=output_text,
    )


@pytest.mark.integration_test
def test_enigma_m3_with_message_from_operation_barbarossa():
    input_text_1 = "EDPUD NRGYS ZRCXN UYTPO MRMBO FKTBZ REZKM LXLVE FGUEY SIOZV EQMIK UBPMM YLKLT TDEIS MDICA GYKUA CTCDO MOHWX MUUIA UBSTS LRNBZ SZWNR FXWFY SSXJZ VIJHI DISHP RKLKA YUPAD TXQSP INQMA TLPIF SVKDA SCTAC DPBOP VHJK"
    output_text_1 = "AUFKL XABTE ILUNG XVONX KURTI NOWAX KURTI NOWAX NORDW ESTLX SEBEZ XSEBE ZXUAF FLIEG ERSTR ASZER IQTUN GXDUB ROWKI XDUBR OWKIX OPOTS CHKAX OPOTS CHKAX UMXEI NSAQT DREIN ULLXU HRANG ETRET ENXAN GRIFF XINFX RGTX"

    input_text_2 = "SFBWD NJUSE GQOBH KRTAR EEZMW KPPRB XOHDR OEQGB BGTQV PGVKB VVGBI MHUSZ YDAJQ IROAX SSSNR EHYGG RPISE ZBOVM QIEMM ZCYSG QDGRE RVBIL EKXYQ IRGIR QNRDN VRXCY YTNJR"
    output_text_2 = "DREIG EHTLA NGSAM ABERS IQERV ORWAE RTSXE INSSI EBENN ULLSE QSXUH RXROE MXEIN SXINF RGTXD REIXA UFFLI EGERS TRASZ EMITA NFANG XEINS SEQSX KMXKM XOSTW XKAME NECXK"

    enigma = EnigmaM3()
    enigma.setup(
        reflector="B",
        rotors="II IV V",
        ring_settings="2 21 12",
        plugboard_pairs="AV BS CG DL FU HZ IN KM OW RX",
        starting_positions="BLA",
    )
    assert enigma.encode(input_text_1) == output_text_1.replace(" ", "")
    enigma.set_rotor_positions("LSD")
    assert enigma.encode(input_text_2) == output_text_2.replace(" ", "")
