import math
import os.path
from pathlib import Path
import csv
import json
from random import randint
from typing import Callable


def _csv_generator(func: Callable):
    rows = []
    for i in range(100, randint(101, 1000 + 1)):
        to_write = (randint(1, 100) for _ in range(3))
        rows.append([*to_write])

    fieldnames = ['num1', 'num2', 'num3']
    dir_name = os.path.basename(os.getcwd())
    file = Path(f"{dir_name}.csv")

    def wrapper(*args, **kwargs):
        with open(file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            for row in rows:
                writer.writerow(row)
            result = func(f, *args, **kwargs)
        return result
    return wrapper


@_csv_generator
def csv_decorator(file: Path, func: Callable):

    def wrapper(*args, **kwargs):
        dir_name = os.path.basename(os.getcwd())
        file_csv = Path(f"{dir_name}.csv")
        if file_csv.is_file():
            with open(file_csv, 'r', encoding='utf-8') as f:
                csv_reader = list(csv.reader(f))[1:]
        result = func(csv_reader, *args, **kwargs)

        return result

    return wrapper


def json_deco(func: Callable):
    dir_name = os.path.basename(os.getcwd())
    file_json = Path(f"{dir_name}.json")

    def wrapper(*args, **kwargs):
        dct = {}
        result = func(*args, **kwargs)
        for key, val in result.items():
            dct[key] = val
        with open(file_json, 'w', encoding='utf-8') as j_f:
            json.dump(dct, j_f, indent=2)

        return result
    return wrapper


@csv_decorator
@json_deco
def root_finder(lst: list[int]):
    solutions = {}
    for step in lst:
        a, b, c = int(step[int(0)]), int(step[1]), int(step[2])
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            solutions[f'{a = }, {b = }, {c = }'] = str([f"{x1:.2f}, {x2:.2f}"])
        elif discriminant == 0:
            x = -b / (2 * a)
            solutions[f'{a = }, {b = }, {c = }'] = str(x)
        else:
            solutions[f'{a = }, {b = }, {c = }'] = "No roots"

    return solutions


root_finder()
