import numpy as np
import matplotlib.pyplot as plt


def f1(x):

    y = x * x
    zerosx = []

    for i in range(len(x)):
        if y[i] == 0:
            zerosx.append(i)

    plt.plot([zerosx[i] for i in range(len(zerosx))], 0, 'rs')

    return y

a = np.array([i for i in range(-100, 101)])
a = a/10

plt.plot(f1(a))
plt.show()
