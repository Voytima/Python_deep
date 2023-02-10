"""
📌 Напишите функцию для транспонирования матрицы
"""


def matrix_transpose(mtrx):
    trans_mtrx = [[0 for _ in range(len(mtrx))] for _ in range(len(mtrx[0]))]
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            trans_mtrx[j][i] = mtrx[i][j]
    print("Transpose matrix:")
    for row in trans_mtrx:
        print(*row)
    print()


def matrix_printer(mtrx):
    print("Original matrix:")
    for row in mtrx:
        print(*row)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]
matrix_transpose(matrix)
matrix_printer(matrix)
