"""Specific Enigma models."""


from .enigma_model import EnigmaModel, PresetReflector, PresetRotor


class RotorI(PresetRotor):
    """Enigma M3 Rotor I."""

    set_wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    turnover_positions = ["R"]


class RotorII(PresetRotor):
    """Enigma M3 Rotor II."""

    set_wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    turnover_positions = ["F"]


class RotorIII(PresetRotor):
    """Enigma M3 Rotor III."""

    set_wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    turnover_positions = ["W"]


class RotorIV(PresetRotor):
    """Enigma M3 Rotor IV."""

    set_wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    turnover_positions = ["K"]


class RotorV(PresetRotor):
    """Enigma M3 Rotor V."""

    set_wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
    turnover_positions = ["A"]


class RotorVI(PresetRotor):
    """Enigma M3 Rotor VI."""

    set_wiring = "JPGVOUMFYQBENHZRDKASXLICTW"
    turnover_positions = ["A", "N"]


class RotorVII(PresetRotor):
    """Enigma M3 Rotor VII."""

    set_wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
    turnover_positions = ["A", "N"]


class RotorVIII(PresetRotor):
    """Enigma M3 Rotor VIII."""

    set_wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
    turnover_positions = ["A", "N"]


class ReflectorA(PresetReflector):
    """Enigma M3 Reflector A."""

    set_wiring = "EJMZALYXVBWFCRQUONTSPIKHGD"


class ReflectorB(PresetReflector):
    """Enigma M3 Reflector B."""

    set_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


class ReflectorC(PresetReflector):
    """Enigma M3 Reflector C."""

    set_wiring = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


class M3(EnigmaModel):
    """The Army M3 Enigma."""

    available_rotors = {
        "I": RotorI,
        "II": RotorII,
        "III": RotorIII,
        "IV": RotorIV,
        "V": RotorV,
        "VI": RotorVI,
        "VII": RotorVII,
        "VIII": RotorVIII,
    }

    available_reflectors = {"A": ReflectorA, "B": ReflectorB, "C": ReflectorC}
