"""Главная программа расчёта кирпичей."""
from builder.bricks import Brick
from builder.wall import Wall
from utils.constants import STANDARD_BRICK, STANDARD_MORTAR

def main():
    # Создаём объекты
    brick = Brick(*STANDARD_BRICK, STANDARD_MORTAR)
    wall = Wall(10000, 510, 3000)
    
    # Объёмный метод (ваш оригинал)
    vol_wall = wall.volume_m3
    vol_brick = brick.volume_with_mortar_m3()
    quantity_volume = round(vol_wall / vol_brick)
    
    # Линейный метод
    bricks_length = round(wall.bricks_in_length(brick.with_mortar_m[0]))
    bricks_thickness = round(wall.bricks_in_thickness(brick.with_mortar_m[1]))
    rows = round(brick.rows_in_height(wall.dimensions_mm[2] / 1000))
    
    bricks_row = bricks_length * bricks_thickness
    quantity_linear = bricks_row * rows
    
    print(f"📦 ОБЪЁМНЫЙ МЕТОД: {quantity_volume:,} кирпичей")
    print(f"📏 ЛИНЕЙНЫЙ МЕТОД: {quantity_linear:,} кирпичей")
    print(f"💡 РЕКОМЕНДУЕМЫЙ: {quantity_linear:,} шт. + 10% = {quantity_linear * 1.1:,.0f} шт.")

if __name__ == "__main__":
    main()