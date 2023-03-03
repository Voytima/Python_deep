"""
📌 Создайте класс Матрица.
📌 Добавьте методы для:
    ○ вывода на печать;
    ○ сравнения;
    ○ сложения;
    ○ * умножения матриц.
"""
import random


class Matrix:
    """
    Class is able to create object type matrix and perform some operations with matrices like:
        print matrices;
        check two matrices for equality;
        two matrices addition;
        two matrices multiplication.
    """

    def __init__(self, row=None, col=None, res=None):
        """
        Base matrix constructor.

        Matrix can be created either by entering numbers of columns and rows or entering list of lists.
        :param row: int | None
        :param col: int | None
        :param res: list[list[int]] | None
        """
        self.row = row
        self.col = col
        self.res = res
        if res is not None:
            self.matrix = res
        else:
            self.matrix = [[random.randrange(0, 10) for _ in range(col)] for _ in range(row)]

    def __str__(self):
        """Returns matrix in non-linear form"""
        res_matrix = '\n'.join(['\t'.join(map(str, lst)) for lst in self.matrix])
        return f"{Matrix.__name__}:\n{res_matrix}"

    def __add__(self, other):
        """
        Addition of two matrices.

        Firstly method checks matrices for rows and columns equality.
        If matrices are not equal in rows or columns, addition cannot be performed.
        Method performs addition for each element on the same positions in two matrices.
        :param other: list[list[int]]
        :return: list[list[int]]
        """
        if len(self.matrix) == len(other.matrix):

            length = len(self.matrix[0])
            for row in self.matrix:
                if len(row) != length:
                    return f"Cannot do addition with different size matrices"
            for row2 in other.matrix:
                if len(row2) != length:
                    return f"Cannot do addition with different size matrices"
            result = []
            temp = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    _sum = other.matrix[i][j] + self.matrix[i][j]
                    temp.append(_sum)
                    if len(temp) == len(self.matrix[0]):
                        result.append(temp)
                        temp = []
            return Matrix(res=result)
        else:
            return f"Cannot do addition with different size matrices"

    def __mul__(self, other):
        """
        Multiplication of two matrices.

        Firstly method checks matrices for equality. Number of columns in first matrix
        should be equal to number of rows in the second matrix.
        If matrices are not equal, multiplication cannot be performed.
        Multiplication principle:
            cij = sum(air * brj) = ai1 * b1j + ai2 * b2j + ... + aim * bmj for r = 1 to m, where
            a - first matrix
            b - second matrix

        :param other: list[list[int]]
        :return: list[list[int]]
        """
        rows_self = len(self.matrix)
        col_self = len(self.matrix[0])
        rows_other = len(other.matrix)
        col_other = len(other.matrix[0])

        if col_self == rows_other:
            result = [[0 for _ in range(col_other)] for _ in range(rows_self)]
            for row in range(rows_self):
                for col in range(col_other):
                    for j in range(col_self):
                        result[row][col] += self.matrix[row][j] * other.matrix[j][col]
            return Matrix(res=result)
        else:
            return f"Multiplication impossible\nMatrices have different number columns and rows"

    def __eq__(self, other):
        """Return True if both matrices are equal or False otherwise"""
        return True if self.matrix == other.matrix else False

    def __gt__(self, other):
        """Return True if first matrix greater than second matrix or False otherwise"""
        return True if self.matrix > other.matrix else False

    def __ge__(self, other):
        """Return True if first matrix greater or equal to second matrix or False otherwise"""
        return True if self.matrix >= other.matrix else False


if __name__ == '__main__':
    m1 = Matrix(res=[[1, 2], [2, 3]])
    m2 = Matrix(res=[[1, 2], [2, 3]])
    # m1 = Matrix(2, 3)
    # m2 = Matrix(2, 3)
    print(m1)
    print(m2)
    m3 = m1 + m2
    print(m3)
    m4 = m1 * m2
    print(m4)
    print(m1 == m2)
