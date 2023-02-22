"""
📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Распечатайте его как pickle строку.
"""
import csv
import pickle

with open('csv_out.csv', 'r', encoding='utf-8') as csv_f:
    data = csv.reader(csv_f)
    to_print = []
    for i in data:
        to_print.append(i)

    print(pickle.dumps(to_print))
