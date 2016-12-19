# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

mu1 = np.array([1, 1])
mu2 = np.array([2, 2])

cov1 = np.array([[1, 0],
                 [0, 1]])
cov2 = np.array([[1, 0],
                 [0, 1]])

x = np.linspace(-5, 5, 1000)

y_list = []
for i in range(100):
    w = np.random.multivariate_normal(mu1, cov1)
    y_list.append(x * w[1] + w[0])

for y in y_list:
    plt.plot(x, y, c="b", alpha=0.25)
