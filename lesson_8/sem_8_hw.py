"""
📌 Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
    файлов и директорий.
"""
__all__ = ['traversal']

import os
import pathlib
import json
import csv
import pickle


def traversal(work_dir: pathlib.Path, save_dir: pathlib.Path):
    all_files = pathlib.Path(work_dir).glob('**/*')
    data = {}
    for file in all_files:
        if file.is_dir():
            f_type = 'dir'

            def _folder_size(check_dir):
                b_size = 0
                for f in pathlib.Path(check_dir).rglob('*'):
                    if os.path.isfile(f):
                        b_size += os.path.getsize(f)

                return b_size

            size = _folder_size(file)

        elif file.is_file():
            f_type = 'file'
            size = file.stat(follow_symlinks=False).st_size
        else:
            f_type = ''
            size = 0
        data[f"{str(file.name)}"] = {"type": f_type, "size": size, 'parent': str(file.parent).split('\\')[-1]}

    rows = []
    for file_name, value in data.items():
        rows.append({'file_name': file_name, 'file_type': value['type'], 'file_size': value['size'],
                     'parent': value['parent']})

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    j_path = os.path.join(save_dir, '%s' % 'trav.json')
    csv_path = os.path.join(save_dir, '%s' % 'trav.csv')
    pkl_path = os.path.join(save_dir, '%s' % 'trav.pkl')

    with (
        open(j_path, 'w', encoding='utf8') as j_file,
        open(csv_path, 'w', encoding='utf-8', newline="") as csv_file,
        open(pkl_path, 'wb') as pckl_file
    ):
        json.dump(data, j_file, indent=2)
        pickle.dump(data, pckl_file)
        fieldnames = ['file_name', 'file_type', 'file_size', 'parent']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    directory = 'files_and_folders'
    traversal(pathlib.Path('E:\\GB\\PY_projects\\Python_deep\\lesson_8'), pathlib.Path(directory))
