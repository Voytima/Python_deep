"""
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from pathlib import Path
from random import choice, randint

VOWELS = 'aeiouy'
CONSTANTS = 'bcdfghjklmnpqrstvwxz'


def str_filler(count: int, str_len_min: int, str_len_max: int, file: str | Path):
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            rnd_name = "".join(choice(VOWELS) if i % 3 == 0 else choice(CONSTANTS) for i in range(
                randint(str_len_min, str_len_max))).capitalize()
            f.write(f"{rnd_name}\n")


if __name__ == '__main__':
    str_filler(10, 4, 7, Path('rnd_names.txt'))
