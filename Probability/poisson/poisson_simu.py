# coding:utf-8
from scipy.stats import bernoulli, poisson
import matplotlib.pyplot as plt
import numpy as np


N = 10000
l = 3
p = l / float(N)


def make_sample(M=1000):
    log = np.sum(bernoulli(p).rvs(size=[N, M]), axis=0)
    return log


def make_poisson():
    x = np.array(range(20))
    x = np.linspace(0, 20, 20)
    p = poisson.pmf(x, l)
    print x
    print p
    return p

sample_log = make_sample()
plt.hist(sample_log, normed=True, bins=10)
plt.plot(np.linspace(0, 20, 20), make_poisson())
plt.show()
