"""
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""
__all__ = ['files_combine']
from pathlib import Path
from typing import TextIO


def _read_or_back(fd: TextIO) -> str:
    line = fd.readline()
    if line == '':
        fd.seek(0)
        return _read_or_back(fd)
    return line[:-1]


def files_combine(nums: str | Path, strings: str | Path, res: str | Path):
    with (
        open(nums, 'r', encoding='utf-8') as f_nums,
        open(strings, 'r', encoding='utf-8') as f_str,
        open(res, 'w', encoding='utf-8') as f_res
    ):
        len_str = sum(1 for _ in f_str)
        len_num = sum(1 for _ in f_nums)

        for _ in range(max(len_num, len_str)):
            name = _read_or_back(f_str)
            two_nums = _read_or_back(f_nums)
            num_i, num_f = two_nums.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_res.write(f"{name.lower()} {-mult}\n")
            elif mult > 0:
                f_res.write(f"{name.upper()} {int(-mult)}\n")


if __name__ == '__main__':
    files_combine(Path('numbers.txt'), Path('rnd_names.txt'), Path('result.txt'))
