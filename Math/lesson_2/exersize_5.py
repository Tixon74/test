import numpy as np
import matplotlib.pyplot as plt


def f1(x, y):
    z = x * x * np.sin(y)
    return z


def plot_func(f, a, b):
    x = np.array([i for i in range(a, b)])
    y = np.array([i for i in range(a, b)])

    local_min = []
    local_max = []

    z = np.zeros((int(b - a), int(b - a)))

    for i in range(a, b):
        for j in range(a, b):
            z[i, j] = f(i, j)

    plt.figure('global_max')

    for i in range(a, b):
        global_max = max(z[i])
        for j in range(a, b):
            if z[i, j] == global_max:
                plt.plot(i, z[i, j], 'ys')

    plt.figure('global_min')

    for i in range(a, b):
        global_min = min(z[i])
        for j in range(a, b):
            if z[i, j] == global_min:
                plt.plot(i, z[i, j], 'bs')

    return np.array(y)

    global_max = max(z.all())
    global_min = min(z.all())

    plt.figure('local_max')

    for i in range(a, b):
        for j in range(a, b):
            if z[i, j] > z[i + 1, j] and z[i, j] > z[i - 1, j] and z[i, j] > z[i, j + 1] and z[i, j] > z[i, j - 1] and z[i, j] != global_max:
                plt.plot(i, z[i, j], 'gs')

    plt.figure('local_min')

    for i in range(a, b):
        for j in range(a, b):
            if z[i, j] < z[i + 1, j] and z[i, j] < z[i - 1, j] and z[i, j] < z[i, j + 1] and z[i, j] < z[i, j - 1] and z[i, j] != global_min:
                plt.plot(i, z[i, j], 'rs')

plot_func(f1, -100, 100)

plt.show()
