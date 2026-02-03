"""Модуль работы с размерами кирпича и раствора."""

from typing import Tuple
from utils.constants import MM_TO_M

def add_mortar(dimensions: Tuple[float, float, float], mortar: float) -> Tuple[float, float, float]:
    """Добавляет толщину раствора к каждому измерению."""
    return tuple(d + mortar for d in dimensions)

def convert_to_meters(dimensions: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """Переводит из мм в метры."""
    return tuple(d * MM_TO_M for d in dimensions)