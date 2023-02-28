"""
📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра.
"""
import csv
import json
import os.path
from pathlib import Path


class Person:
    """ For object creation file name is required """

    def __init__(self, file, access_level=None, user_id=None, name=None):
        self.file = None
        self.access_level = access_level
        self.user_id = user_id
        self.name = name
        self.file = Path(f"{file}.json")

    def user_add(self) -> None:
        unique_id = set()
        res = {str(i): {} for i in range(1, 7 + 1)}

        if self.file.is_file() and os.path.getsize(self.file) > 0:
            with open(self.file, 'r', encoding='utf-8') as f:
                res = json.load(f)
                unique_id.update(*((value.keys()) for value in res.values()))

        while True:
            try:
                self.access_level, self.user_id, self.name = input("Enter access lvl, id and name\n>>> ").split()
                if self.user_id in unique_id:
                    print("Такой id уже существует\n")
                    continue
                res[self.access_level].update({int(self.user_id): self.name})
                with open(self.file, 'w', encoding='utf-8') as f:
                    json.dump(res, f, indent=2)
                    print("Confirmed, written...\n")
            except KeyboardInterrupt:
                print("Have a nice day!")
                break

    def get_from_user(self) -> None:
        json_file = {}
        if os.path.isfile(self.file):
            with open(self.file, 'r', encoding='utf-8') as js:
                if os.path.getsize(self.file) > 0:
                    json_file = json.load(js)

        rows = []
        for level, value in json_file.items():
            for u_id, name in value.items():
                rows.append({'access_level': level, 'user_id': u_id, 'name': name})

        with open(Path(f"{str(self.file).split('.')[0]}.csv"), 'w', encoding='utf-8', newline="") as f:
            fieldnames = ['access_level', 'user_id', 'name']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


if __name__ == '__main__':
    users_file = input("Enter file name: ")
    users = Person(users_file)
    users.user_add()
    users.get_from_user()
