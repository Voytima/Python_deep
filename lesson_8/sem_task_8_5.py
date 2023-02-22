"""
📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import os
import pickle
from pathlib import Path


def file_rename(extension: str, w_dir: str | Path) -> None:
    for file in os.listdir(w_dir):
        if file.endswith(extension):
            file_name = file.split('.')[0]
            with open(file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                with open(f'{file_name}.pkl', mode='wb') as file_pkl:
                    pickle.dump(data, file_pkl)


if __name__ == '__main__':
    ext = 'json'
    # folder = r'E:\GB\PY_projects\Python_deep\lesson_8'
    folder = input("Enter folder path to search json files: ")
    file_rename(ext, Path(folder))














