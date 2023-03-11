"""
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""
from collections import deque

from lesson_13.sem_13_hw_1_1 import DequeLengthError, ValueTypeError


class Factorial:
    def __init__(self, k: int):
        if not isinstance(k, int):
            raise ValueTypeError(k)
        if k >= 0:
            self.memory = deque(maxlen=k)
        else:
            raise DequeLengthError(k)

    def __call__(self, n):
        if not isinstance(n, int):
            raise ValueTypeError(n)
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return result

    def printer(self):
        return self.memory


if __name__ == '__main__':
    f = Factorial(3)
    print(f(5))
    print(f(0))
    print(f(3))
    print(f(7))
    print(f.printer())
