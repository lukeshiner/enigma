"""Models of enigma."""

from typing import Type

from .enigma_model import EnigmaModel
from .m3 import M3, M3Army

__all__ = ["EnigmaModel", "M3", "M3Army"]

models: dict[str, Type[EnigmaModel]] = {"M3": M3, "M3Army": M3Army}
