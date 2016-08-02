# coding:utf-8
from scipy.stats import norm

import matplotlib.pyplot as plt
import numpy as np

a = 0.1
b = 0

mu = 0.0
sigma_x = 100.0
sigma_yx = 1.0

y = 1.0

sigma_xy = ((1 / sigma_x ** 2 + a ** 2 / sigma_yx ** 2) ** -1) ** 0.5

mu_xy = sigma_xy ** 2 / sigma_yx ** 2 * \
    (a * (y - b) + sigma_yx ** 2 / sigma_x ** 2 * mu)

x = np.linspace(mu_xy - sigma_xy * 3, mu_xy + sigma_xy * 3, 1000)
y = norm(mu_xy, sigma_xy).pdf(x)

print mu_xy, sigma_xy


plt.plot(x, y)
plt.show()
