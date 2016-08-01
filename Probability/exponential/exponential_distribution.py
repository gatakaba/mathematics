# coding:utf-8

from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

for l in range(1, 10):

    x = np.linspace(0, 3, 100)
    p = expon(scale=l ** -1).pdf(x)

    plt.plot(x, p)

plt.show()
