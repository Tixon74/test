import numpy as np


def func(matrix1, matrix2):
    shape1 = matrix1.shape
    shape2 = matrix2.shape

    if shape1[1] != shape2[0]:
        return np.array([])

    out_matrix = np.zeros((shape1[0], shape2[1]))

    for i in range(shape1[0]):
        for j in range(shape2[1]):
            summ = 0
            for t in range(shape1[1]):
                summ += matrix1[i, t] * matrix2[t, j]
                out_matrix[i, j] = summ

    return out_matrix


def func3(matr1, matr2, matr3):
    return func(matr3, func(matr1, matr2))


Matrix1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]])
Matrix2 = np.array([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
Matrix3 = np.array([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])

print(func3(Matrix1, Matrix2, Matrix3))
