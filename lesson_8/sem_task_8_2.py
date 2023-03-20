"""
📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключем для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
import os.path
from pathlib import Path


def user_add(file: Path) -> None:
    unique_id = set()
    res = {str(i): {} for i in range(1, 7 + 1)}

    if file.is_file() and os.path.getsize(file) > 0:
        with open(file, 'r', encoding='utf-8') as f:
            res = json.load(f)
            unique_id.update(*((value.keys()) for value in res.values()))

    while True:
        access_level, user_id, name = input(">>> ").split()
        if user_id in unique_id:
            print("Такой id уже существует")
            continue
        res[access_level].update({int(user_id): name})
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=2)


if __name__ == '__main__':
    user_add(Path('user.json'))
