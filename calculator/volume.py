"""Модуль расчёта объёмов."""
import math
from typing import Tuple

def volume_mm3(dimensions: Tuple[float, float, float]) -> float:
    """Объём в мм³."""
    return math.prod(dimensions)

def volume_m3(dimensions_mm: Tuple[float, float, float]) -> float:
    """Объём в м³ (из мм)."""
    vol_mm3 = volume_mm3(dimensions_mm)
    return vol_mm3 * (1/1000)**3
