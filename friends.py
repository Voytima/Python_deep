"""
📌 Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:
📌 какие вещи взяли все три друга
📌 какие вещи уникальны, есть только у одного друга
📌 какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
📌 Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

friends = {"Bob": ("backpack", "axe", "matches", "boots",),
           "Mike": ("backpack", "matches", "boots",),
           "Mark": ("tent", "backpack", "matches",),
           "Frankie": ("backpack", "matches", "boots",),
           "Polly": ("matches", "backpack", "axe", "boots",),
           }

friends_things = {k: set(v) for k, v in friends.items()}
all_things = set.union(*friends_things.values())

print(f"All friends took {set.intersection(*friends_things.values())}")

things_count = {}
for items in friends_things.values():
    for item in items:
        things_count[item] = things_count.get(item, 0) + 1

for key, val in things_count.items():
    if val == len(friends_things) - 1:
        for name, things in friends_things.items():
            if key not in things:
                print(f"Only {name} didn't take {key}")

for key, val in things_count.items():
    if val == 1:
        print(f"Unique thing is {key}")
