"""Кирпич с раствором."""
from typing import Tuple
from calculator.dimension import add_mortar, convert_to_meters
from calculator.volume import volume_m3

class Brick:
    def __init__(self, length: float, width: float, height: float, mortar: float = 10):
        self.base = (length, width, height)
        self.mortar = mortar
        self.with_mortar_mm = add_mortar(self.base, mortar)
        self.with_mortar_m = convert_to_meters(self.with_mortar_mm)
    
    def volume_with_mortar_m3(self) -> float:
        return volume_m3(self.with_mortar_mm)
    
    def rows_in_height(self, wall_height_m: float) -> float:
        """Количество рядов по высоте."""
        row_height_m = self.with_mortar_m[2]
        return wall_height_m / row_height_m
