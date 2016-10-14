# coding:utf-8
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np


def priorDistribution(mu):
    if 0 < mu < 1:
        return 1
    else:
        return 10 ** -9


def logLikelihood(mu, D):
    if 0 < mu < 1:
        return np.sum(D * np.log(mu) + (1 - D) * np.log(1 - mu))
    else:
        return -np.inf

np.random.seed(0)
sample = 0.5
sample_list = []
burnin_ratio = 0.1
N = 10
# make data
D = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])
l = logLikelihood(sample, D) + np.log(priorDistribution(sample))
# Start MCMC
for i in range(10 ** 6):
    # make candidate sample
    sample_candidate = np.random.normal(sample, 10 ** -2)
    l_new = logLikelihood(sample_candidate, D) + \
        np.log(priorDistribution(sample_candidate))
    # decide accept
    if min(1, np.exp(l_new - l)) > np.random.random():
        sample = sample_candidate
        l = l_new
    sample_list.append(sample)
sample_list = np.array(sample_list)
sample_list = sample_list[int(burnin_ratio * N):]

# calc beta
x = np.linspace(0, 1, 1000)
y = beta.pdf(x, sum(D) + 1, N - sum(D) + 1)

plt.plot(x, y, linewidth=3)
plt.hist(sample_list, normed=True, bins=100)
plt.show()
