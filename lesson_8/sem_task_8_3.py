"""
📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""
import csv
import json
import os
from pathlib import Path


def get_from_user(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []
    for level, value in json_file.items():
        for u_id, name in value.items():
            rows.append({'access_level': level, 'user_id': u_id, 'name': name})

    with open('out.csv', 'w', encoding='utf-8', newline="") as f:
        fieldnames = ['access_level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    get_from_user(Path('./user.json'))
