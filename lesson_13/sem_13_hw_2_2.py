"""
📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""

from lesson_13.sem_13_hw_2_1 import LengthValueError, WidthValueError, LengthTypeError, WidthTypeError


class Rectangle:

    def __init__(self, length, width=None):
        if not isinstance(length, int | float):
            raise LengthTypeError(length)
        if width is not None and not isinstance(width, int | float):
            raise WidthTypeError(width)
        if length > 0:
            self._length = length
        else:
            raise LengthValueError(length)
        if width is not None and width > 0:
            self._width = width
        elif width is None:
            self._width = length
        else:
            raise WidthValueError(width)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length_value):
        if not isinstance(length_value, int | float):
            raise LengthTypeError(length_value)
        if length_value > 0:
            self._length = length_value
        else:
            raise LengthValueError(length_value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width_value):
        if not isinstance(width_value, int | float):
            raise WidthTypeError(width_value)
        if width_value > 0:
            self._width = width_value
        else:
            raise WidthValueError(width_value)


if __name__ == '__main__':
    r = Rectangle(2, 3)
    print(r.perimeter())
    # r.length = -2
    # print(r.length, r.width)
    # print(r.perimeter())
    # r.width = 2
    # print(r.length, r.width)
    # print(r.perimeter())









