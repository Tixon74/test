import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    y = x * x * x / 12 + x * (x - 15) - 72
    return y

a = np.array([i for i in range(-100, 101)])
a = a/10

print(a)

plt.plot(f1(a))
plt.show()
