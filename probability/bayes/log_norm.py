# coding:utf-8
import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt

r = lognorm.rvs(1, loc=10, scale=1, size=10000)

plt.subplot(211)
plt.hist(r, bins=100)
plt.subplot(212)
plt.xscale("log")
plt.hist(np.log(r), bins=100)

plt.show()
