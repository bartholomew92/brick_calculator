"""Стена и кладка."""
from typing import Tuple
from calculator.volume import volume_m3

class Wall:
    def __init__(self, length_mm: float, thickness_mm: float, height_mm: float):
        self.dimensions_mm = (length_mm, thickness_mm, height_mm)
        self.volume_m3 = volume_m3(self.dimensions_mm)
    
    def bricks_in_length(self, brick_length_with_mortar_m: float) -> float:
        """Кирпичей в длину стены."""
        return self.dimensions_mm[0] / (brick_length_with_mortar_m * 1000)
    
    def bricks_in_thickness(self, brick_width_with_mortar_m: float) -> float:
        """Кирпичей по толщине."""
        return self.dimensions_mm[1] / (brick_width_with_mortar_m * 1000)
