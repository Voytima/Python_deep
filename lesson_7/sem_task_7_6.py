"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
from pathlib import Path
from random import choices, randint
from string import ascii_letters, digits
import os


def file_to_dir(extension: str, file_dir: str | Path, min_name: int = 6, max_name: int = 30,
                min_size: int = 256, max_size: int = 4096, count: int = 42):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(count):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        file_path = os.path.join(file_dir, '%s.%s' % (name, extension))

        if file_path not in file_dir:
            data = bytes(randint(0, 255) for _ in range(min_size, max_size))
            with open(file_path, 'wb') as f:
                f.write(data)
        else:
            continue


if __name__ == '__main__':
    directory = input('Куда вы хотите сохранить файл?: ')
    expansion = input('Введите расширение файла: ')

    file_to_dir(expansion, directory)
