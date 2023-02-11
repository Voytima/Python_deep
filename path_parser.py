"""
📌 Напишите функцию, которая принимает на вход строку - абсолютный путь до
файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def string_parser(string: str) -> tuple:
    path = '/'.join(string.split('\\')[:-1])
    *_, file_name, file_extension = string.split('\\')[-1].split('.')

    return path, file_name, file_extension


abs_path = r"E:\GB\PY_projects\Python_deep\atm.py"
print(string_parser(abs_path))
