from matplotlib import pyplot as plt

from scipy.stats import uniform, norm
from sklearn.mixture import GMM

import numpy as np


def likelihood(a, b, X):
    return np.exp(np.sum(np.log((1 - a) * norm(0, sigma).pdf(X) + a * norm(b, sigma).pdf(X))))

a, b = 0.1, 1
sigma = 1
gmm = GMM(2)
gmm.means_ = np.array([[0], [b]])
gmm.covars_ = np.array([[sigma], [sigma]])
gmm.weights_ = np.array([1 - a, a])

X = gmm.sample(100)
a = np.linspace(0, 1, 100)
b = np.linspace(-5, 5, 100)

aa, bb = np.meshgrid(a, b)
lp = []
for p in np.c_[np.ravel(aa), np.ravel(bb)]:
    lp.append(likelihood(p[0], p[1], X))

lp = np.array(lp).reshape(*aa.shape)

lp = lp / (np.sum(lp))


plt.subplot(2, 2, 1)
plt.hist(X, bins=30)
plt.subplot(2, 2, 4)
plt.pcolor(aa, bb, lp)
plt.subplot(2, 2, 2)
plt.plot(a, np.sum(lp, axis=0) / np.sum(np.sum(lp, axis=0)))
plt.subplot(2, 2, 3)
plt.plot(b, np.sum(lp, axis=1) / np.sum(np.sum(lp, axis=1)))

print np.sum(a * np.sum(lp, axis=0) / np.sum(np.sum(lp, axis=0)))
print np.sum(b * np.sum(lp, axis=1) / np.sum(np.sum(lp, axis=1)))

plt.show()
