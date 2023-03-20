"""
📌 Функция получает на вход словарь с названием компании в
качестве ключа и списком с доходами и расходами (3-10
чисел) в качестве значения.
📌 Вычислите итоговую прибыль или убыток каждой компании.
Если все компании прибыльные, верните истину, а если хотя
бы одна убыточная - ложь.
"""


def income_counter(dct: dict[str: list]) -> bool:
    res = []
    for value in dct.values():
        res.append(sum(value) / len(value))
    if all(i > 0 for i in res):
        return True
    else:
        return False


companies = {
    'Belshina': [50, -20, 35, -89, 100],    # 15.2
    'Belaz': [200, 163, 155, 220],          # 184.5
    'iTeam': [310, -200, -400, 52, -229]    # -93.4
    }

print(income_counter(companies))
