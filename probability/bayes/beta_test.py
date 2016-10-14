# coding:utf-8
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli


def calc_likelihood(x, mu):
    return bernoulli(mu).pmf(x)


def calc_next_state(w, mu, sigma=0.5):
    # 尤度の大きさに比例した確率でサンプルを抽出し、状態遷移を行う。
    k = 1
    w += 10 ** -6
    index = np.random.choice(range(len(mu)), size=len(mu), p=w / np.sum(w))
    x = 1 / float(k) * np.log(mu / (1 - mu))
    x = np.random.normal(x[index], sigma)

    next_state = 1 / (1 + np.exp(-x * k))
    return next_state


def run_pf():
    N = 1000
    observed = np.zeros(N)
    observed[N / float(2):] = 1

    for i in range(0, 10, 2):
        interval = 3
        observed[500 + interval * (i - 1):500 + interval * i] = 1
        observed[500 + interval * i:500 + interval * (i + 1)] = 0

    for i in range(0, 10, 2):
        interval = 3
        observed[800 + interval * (i - 1):800 + interval * i] = 0
        observed[800 + interval * i:800 + interval * (i + 1)] = 1

    observed[830:] = 0
    M = 10000
    mu_list = np.random.uniform(0, 1, size=M)
    w = calc_likelihood(0.5, mu_list)
    result_list = []
    for i in range(N):
        mu_list = calc_next_state(w, mu_list)
        result_list.append(mu_list)
        x = observed[i]
        w = calc_likelihood(x, mu_list)

    means = np.median(result_list, axis=1)
    stds = np.std(result_list, axis=1)
    plt.ylim(-0.2, 1.2)
    plt.plot(observed, linewidth=1)
    plt.fill_between(
        range(N), means - stds, means + stds, color="r", alpha=0.3)
    plt.plot(means, "ro-")

    plt.show()

run_pf()
