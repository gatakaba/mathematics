# coding:utf-8
from scipy.stats import bernoulli

import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns

p = 0.0001
log = []
for i in range(100):
    print(i)
    tmp = bernoulli(p).rvs(size=10 ** 6)
    log = + (np.diff(np.where(tmp == 1)[0]))
print(len(log))
# print np.mean(log)
# print np.var(log)

sns.distplot(log)
plt.show()
