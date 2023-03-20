"""
✔ Напишите функцию группового переименования файлов. Она должна:
    ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    ✔ принимать параметр количество цифр в порядковом номере.
    ✔ принимать параметр расширение исходного файла.
    Переименование должно работать только для этих файлов внутри каталога.
    ✔ принимать параметр расширение конечного файла.
    ✔ принимать диапазон сохраняемого оригинального имени. Например, для диапазона
    [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
    желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os
from pathlib import Path


def file_rename(extension: str, w_dir: str | Path, number: int, saved_let: list, new_name: str) -> None:
    number = (10 ** number) // 10
    for file in os.listdir(w_dir):
        min_l, max_l = saved_let[0], saved_let[1]
        if file.endswith(extension):
            os.rename(f'{w_dir}/{file}', f'{w_dir}/{file[min_l: max_l]}{new_name}{number}.{extension}')
            number = number + 1


if __name__ == '__main__':
    ext = input("Files with which extension should be renamed: ")
    s_n = int(input("How many nums in serial number: "))
    # folder = r'E:\GB\PY_projects\Python_deep\lesson_7\datas'
    lett_range = [int(input("Min letters num ")), int(input("Max letters num "))]
    wished_name = input("What name should files have: ")
    folder = input("Enter folder path for sort: ")
    file_rename(ext, Path(folder), s_n, lett_range, wished_name)












