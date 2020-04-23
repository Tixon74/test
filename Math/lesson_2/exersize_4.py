import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    y = x * x * np.sin(x / 100) + 300 * x
    return y


def get_deriviate(f, a, b):
    x = np.array([i for i in range(a, b)])
    len_x = x.shape[0]

    dy = np.array([f(x[i + 1]) - f(x[i]) for i in range(len_x - 1)])

    return dy


def plot_vect(y, a, b):
    x = np.array([i for i in range(a, b)])

    plt.plot(x, y)
    plt.figure()


def plot_func(f, a, b):
    x = np.array([i for i in range(a, b)])
    y = [f(i) for i in x]
    plot_vect(y, a, b)

    return np.array(y)


def plot_func_with_extremums(y, a, b):
    # Формируем x и y
    x = np.array([i for i in range(a, b)])

    global_mins = []
    global_maxs = []

    min_y = min(y)
    max_y = max(y)

    for i in range(len(y)):

        if y[i] == min_y:
            global_mins.append(i)

        if y[i] == max_y:
            global_maxs.append(i)

    # Выводим график y
    plt.plot(x, y)

    # Выводим глобальный минимум
    plt.plot([x[i] for i in global_mins],
             [y[i] for i in global_mins],
             'gs')

    # Выводим глобальный максимум
    plt.plot([x[i] for i in global_maxs],
             [y[i] for i in global_maxs],
             'rs')

dy = get_deriviate(f1, -1000, 1000)
plot_func_with_extremums(dy, -999, 1000)
plot_vect(dy, -999, 1000)
plot_func(f1, -1000, 1000)

plt.show()
