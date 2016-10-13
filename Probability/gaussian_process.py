# coding:utf-8
# ガウス過程の習作

import numpy as np
import matplotlib.pyplot as plt


class GaussianProcess():
    def __init__(self):
        # ノイズ精度(分散の逆)
        self.beta = 10

    def kernel(self, x1, x2):
        return np.exp(-0.5 * np.dot((x1 - x2), (x1 - x2)) * 64) + np.dot(x1, x2) * 5

    def fit(self, x_sample, y_sample):
        self.n_sample = len(x_sample)
        self.x_sample = x_sample
        self.y_sample = y_sample

        self.C = np.zeros([self.n_sample, self.n_sample])

        for i in range(self.n_sample):
            for j in range(self.n_sample):
                self.C[i, j] = self.kernel(x_sample[i], x_sample[j])

        self.C += np.eye(N) * self.beta ** -1

    def predict(self, x_test):
        k = np.zeros(self.n_sample)
        for i in range(self.n_sample):
            k[i] = self.kernel(self.x_sample[i], x_test)

        c = self.kernel(x_test, x_test) + self.beta ** -1

        m = k.T @ np.linalg.inv(self.C) @ self.y_sample
        sigma = c - k.T @ np.linalg.inv(self.C) @ k
        return m, sigma


N = 10
x_sample = np.random.random(size=N)
# x_sample = np.random.normal(0.5, 0.01, size=N)

y_sample = np.sin(2 * np.pi * x_sample) + np.random.normal(0, 0.01, size=N)
gp = GaussianProcess()
gp.fit(x_sample, y_sample)

x = np.linspace(0, 1, 100)
y = []
y_sigma = []

for i in x:
    mu, sigma = gp.predict(i)
    y.append(mu)
    y_sigma.append(sigma)

y = np.array(y)
y_sigma = np.array(y_sigma)

plt.plot(x_sample, y_sample, "ro")
plt.plot(x, y)

plt.fill_between(x, y - y_sigma, y + y_sigma, alpha=0.25)
plt.show()
