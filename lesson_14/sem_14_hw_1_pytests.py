from math import pi
import pytest


def test_area():
    c1 = Circumference(5)
    assert c1.area() == 78.5


def test_perimeter():
    c1 = Circumference(5)
    assert c1.perimeter() == 31.4


class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return round(2 * pi * self.radius, 1)

    def area(self):
        return round(pi * self.radius * self.radius, 1)


if __name__ == '__main__':
    pytest.main(['-vv'])
