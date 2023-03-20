"""
📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import argparse
import os
import pathlib
from pathlib import Path
from collections import namedtuple
import logging

logging.basicConfig(filename="tracker.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def collector(user_dir: pathlib.Path):
    Object = namedtuple('Object', 'ObjectName, Extension, Catalog_flag, Parent_dir')
    all_files = pathlib.Path(user_dir).glob('*')
    for file in all_files:
        if file.is_file():
            file_name = file.name.split('.')[0]
            file_extension = f".{file.name.split('.')[1]}" if str(file.name).count('.') == 1 else None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent_dir = str(file.parent).split('\\')[-1]
            to_write = Object._make([file_name, file_extension, catalog_flag, parent_dir])
            logger.info(to_write)
        elif file.is_dir():
            file_name = file.name
            file_extension = None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent_dir = str(file.parent).split('\\')[-1]
            to_write = Object._make([file_name, file_extension, catalog_flag, parent_dir])
            logger.info(to_write)


def parser():
    parser = argparse.ArgumentParser(description="Обход папок и файлов в указанной директории")
    parser.add_argument('-p', '--path', default=Path(os.getcwd()))
    args = parser.parse_args()
    user_dir = Path(input("Enter path: "))
    path = user_dir if user_dir.is_dir() else args.path
    return collector(path)


if __name__ == '__main__':
    # name = Path(input("Enter path: "))
    # print(collector(name))
    parser()
