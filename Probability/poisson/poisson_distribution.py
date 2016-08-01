# coding:utf-8

from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

for l in range(10):
    x = np.array(range(10))
    p = poisson.pmf(x, l)

    plt.plot(p)

plt.show()
