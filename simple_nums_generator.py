"""
📌 Создайте функцию-генератор.
📌 Функция генерирует N простых чисел, начиная с числа 2.
📌 Для проверки числа на простоту используйте правило:
“число является простым, если делится нацело только на единицу и на себя”.
"""


def simple_nums_generator(n: int) -> int:
    for num in range(2, n + 1):
        d = 0
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                d += 1
                break
        if d == 0:
            yield num


number = int(input("Generate simple numbers form 2 to:\n>>> "))
for i in simple_nums_generator(number):
    print(i)
