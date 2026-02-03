import math

brick_lwh = (250, 120, 65)  # габариты кирпича
mortar = 10  # толщина раствора
wall_lwh = (10000, 510, 3000)  # габариты стены

brick_with_mortar = tuple(
    i + mortar for i in brick_lwh
)  # габариты кирпича + слой раствора


def volume_element():   # объем одного кирпича с раствором
    volume = 1
    for i in brick_with_mortar:
        volume *= i
    return volume


vol_elem = volume_element()


def volume_wall():      # объем стены
    volume = 1
    for i in wall_lwh:
        volume *= i
    return volume


vol_wall = volume_wall()


def quantity_brick(vol_wall, vol_elem):   # количество кирпичей
    q = vol_wall / vol_elem
    return math.ceil(q)


quant_brick = quantity_brick(vol_wall, vol_elem)
print(quant_brick)
