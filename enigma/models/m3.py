"""Specific Enigma models."""

from .enigma_model import EnigmaModel, PresetReflector, PresetRotor


class RotorI:
    """Enigma M3 Rotor I."""

    wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    turnover_positions = ['R']


class RotorII(PresetRotor):
    """Enigma M3 Rotor II."""

    wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    turnover_positions = ['F']


class RotorIII(PresetRotor):
    """Enigma M3 Rotor III."""

    wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    turnover_positions = ['W']


class RotorIV(PresetRotor):
    """Enigma M3 Rotor IV."""

    wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
    turnover_positions = ['K']


class RotorV(PresetRotor):
    """Enigma M3 Rotor V."""

    wiring = 'VZBRGITYUPSDNHLXAWMJQOFECK'
    turnover_positions = ['A']


class RotorVI(PresetRotor):
    """Enigma M3 Rotor VI."""

    wiring = 'JPGVOUMFYQBENHZRDKASXLICTW'
    turnover_positions = ['A', 'N']


class RotorVII(PresetRotor):
    """Enigma M3 Rotor VII."""

    wiring = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
    turnover_positions = ['A', 'N']


class RotorVIII(PresetRotor):
    """Enigma M3 Rotor VIII."""

    wiring = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
    turnover_positions = ['A', 'N']


class ReflectorA(PresetReflector):
    """Enigma M3 Reflector A."""

    wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD'


class ReflectorB(PresetReflector):
    """Enigma M3 Reflector B."""

    wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'


class ReflectorC(PresetReflector):
    """Enigma M3 Reflector C."""

    wiring = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'


class M3(EnigmaModel):
    """The Army M3 Enigma."""

    rotors = {
        'I': RotorI,
        'II': RotorII,
        'III': RotorIII,
        'IV': RotorIV,
        'V': RotorV,
        'VI': RotorVI,
        'VII': RotorVII,
        'VIII': RotorVIII
    }

    reflectors = {'A': ReflectorA, 'B': ReflectorB, 'C': ReflectorC}
