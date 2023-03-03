"""
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""


class Rectangle:
    """
    Class supports an object type rectangle creation as well as
    supports addition and subtraction perimeters of two rectangles and
    returns new object type rectangle.
    """

    def __init__(self, length, width=None):
        self.length = length
        self.width = width or length

    def area(self):
        """Calculates area of the rectangle."""
        return self.width * self.length

    def perimeter(self):
        """Calculates perimeter of the rectangle."""
        return 2 * (self.width + self.length)

    def __add__(self, other):
        """
        Calculates two rectangle perimeters addition.

        new_perimeter calculates addition of two rectangle perimeters.
        new_width and new_length calculate width and length for new
        object type rectangle.
        :param other:
        :return: new object type rectangle
        """
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        """
        Calculates two rectangle perimeters subtraction.

        new_perimeter calculates an absolute value of subtraction of two rectangle perimeters.
        new_width and new_length calculate absolute value of width and length for new
        object type rectangle.
        :param other:
        :return: new object type rectangle
        """
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __eq__(self, other):
        """
        Compare areas of two rectangles and return True if they are
        equal in their areas and False if they are not.

        :param other:
        :return: True of False
        """
        return self.area() == other.area()

    def __gt__(self, other):
        """
        Compare areas of two rectangles and return True if area
        of first rectangle is greater than area of the second rectangle.

        :param other:
        :return: True of False
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare areas of two rectangles and return True if area
        of first rectangle is greater than or equal to area of the second rectangle.

        :param other:
        :return: True of False
        """
        return self.area() >= other.area()


if __name__ == '__main__':
    r1 = Rectangle(3)
    r2 = Rectangle(3)
    print(r1.perimeter())
    print(r2.perimeter())
    r3 = r2 + r1
    # print(r3.perimeter())
    r4 = r2 - r1
    # print(f"{r4.perimeter() = }")
    # print(r1 + r2)
    # print(r1 - r2)
    print(r1 == r2)



