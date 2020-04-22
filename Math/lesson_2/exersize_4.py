import numpy as np
import matplotlib.pyplot as plt


def f2(f, a):
    len_x = a.shape[0] - 1

    dy = np.array([f(a[i + 1]) - f(a[i]) for i in range(len_x)])

    return dy


def f1(x):
    y = x * x * x
    return y


a = np.array([i for i in range(-100, 101)])
a = a / 10

print(len(a))

plt.plot(f2(f1, a))
plt.show()