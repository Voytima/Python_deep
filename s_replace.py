"""
📌 Создайте несколько переменных заканчивающихся и не
оканчивающихся на “s”.
📌 Напишите функцию, которая при запуске заменяет
содержимое переменных оканчивающихся на s (кроме
переменной из одной буквы s) на None.
📌 Значения не удаляются, а помещаются в одноимённые
переменные без s на конце.
"""

names = 'Liza', 'Dima', 'Tanya'
dates = [1988, 1993, 2011]
s = 'Just string'
number = 145636
presentation = False


def s_replacer(name, dat, string, numb, pres):
    res = globals()
    variables = {}
    for key, val in res.items():
        if len(key) != 1 and key.endswith('s'):
            res[key] = None
            variables.setdefault(key[:-1], val)

    return variables


print(s_replacer(names, dates, s, number, presentation))
print(f"{names}\n{dates}\n{s}\n{number}\n{presentation}\n")
