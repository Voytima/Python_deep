"""
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
📌 Напишите к ним тесты.
📌 2-5 тестов на задачу в трёх вариантах:
    ○ doctest,
    ○ unittest,
    ○ pytest.
"""
from math import pi


class Circumference:
    """
    >>> c1 = Circumference(5)
    >>> c1.area()
    78.5
    >>> c1.perimeter()
    31.4
    """

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return round(2 * pi * self.radius, 1)

    def area(self):
        return round(pi * self.radius * self.radius, 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
