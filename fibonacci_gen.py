"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci(n: int) -> int:
    a, b = 1, 1
    print(a)
    for _ in range(n - 1):
        a, b = b, a + b
        yield a


num = int(input("How many Fibo nums:\n>>> "))
for i in fibonacci(num):
    print(i)
