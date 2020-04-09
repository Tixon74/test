import numpy as np


def func(matr):
    shape = matr.shape
    matr1 = np.zeros((shape[1], shape[0]))

    for i in range(shape[0]):
        for j in range(shape[1]):
            matr1[j, i] = matr[i, j]

    out_matr = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            summ = 0
            for t in range(shape[1]):
                summ += matr[i, t] * matr1[t, j]
                out_matr[i, j] = summ

    # out_matr1 = np.linalg.inv(out_matr)

    return out_matr


matrix_4_inv = np.array([[4, 1, 3, 1], [3, 5, 2, 1], [2, 6, 4, 1], [1, 2, 3, 1]])

func(matrix_4_inv)

print(matrix_4_inv)
print()
print(np.linalg.inv(func(matrix_4_inv)))
