import numpy as np

matrix = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4]])

def create_matrix(x, y, variable):


    for i in range(y):
        for j in range(x):
            matrix[i, j] = variable
    return matrix

print(create_matrix(3, 4, 12))