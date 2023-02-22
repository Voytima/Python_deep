"""
📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
📌 Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import pickle
import csv
from pathlib import Path


def pkl_to_csv(file_in: str | Path) -> None:
    with open(file_in, 'rb') as file:
        data = pickle.load(file)

    with open('csv_out.csv', 'w', encoding='utf-8', newline="") as f:
        writer = csv.writer(f)
        keys = [key for key in data[0]]
        writer.writerow(keys)
        for dct in data:
            writer.writerow((dct['access_level'], dct['id'], dct['name'], dct['hash']))


if __name__ == '__main__':
    pkl_to_csv(Path('json_in.pkl'))















