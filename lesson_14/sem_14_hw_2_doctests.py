"""
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
    ○ doctest,
    ○ unittest,
    ○ pytest.
"""
from collections import deque


class Factorial:
    """
    >>> f = Factorial(3)
    >>> print(f(1))
    1
    >>> print(f(3))
    6
    >>> print(f(2))
    2
    >>> print(f.printer())
    deque([{1: 1}, {3: 6}, {2: 2}], maxlen=3)
    >>> f = Factorial(2)
    >>> f(2)
    2
    >>> f(3)
    6
    >>> f(1)
    1
    >>> print(f.printer())
    deque([{3: 6}, {1: 1}], maxlen=2)
    """

    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return result

    def printer(self):
        return self.memory


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
