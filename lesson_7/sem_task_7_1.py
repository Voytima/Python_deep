"""
✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random

from random import randint, uniform
from pathlib import Path

MIN_NUM = -1000
MAX_NUM = 1000


def num_filler(count: int, file: str | Path):
    with open(file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)}|{uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    num_filler(10, Path('numbers.txt'))
