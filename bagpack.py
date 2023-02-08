"""
📌 Создайте словарь со списком вещей для похода в качестве ключа и их массой в
качестве значения. Определите какие вещи влезут в рюкзак передав его
максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

things = {
    'water': 2,
    'matches': 1,
    'bread': 5,
    'tent': 15,
    'flashlight': 5,
    'pot': 10
    }

tuple_of_things = tuple(things.keys())
MAX_WEIGHT = 15
ZERO = 0

for i in range(len(tuple_of_things)):
    for j in range(i, len(tuple_of_things)):
        things_now = (*tuple_of_things[:i], tuple_of_things[j])
        weight = ZERO
        for item in things_now:
            weight += things[item]
        if weight <= MAX_WEIGHT:
            print(f"You can take in your backpack {things_now}, total {weight = }")
