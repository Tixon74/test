import numpy as np

Matrix = np.array([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])


def summ_mx_mn(matr):
    shape = matr.shape

    mx = 0
    mn = 1000000

    for i in range(shape[0]):
        for j in range(shape[1]):
            if mx < matr[i, j]:
                mx = matr[i, j]
            if mn > matr[i, j]:
                mn = matr[i, j]

    return mx + mn

print(summ_mx_mn(Matrix))
