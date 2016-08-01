# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as kde
from scipy.stats import norm
N = 1000
sigma = 0.5
sample = np.r_[np.random.normal(-1, sigma, N) , np.random.normal(1, sigma, N) ]
 
x = np.linspace(-5, 5, 1000)
y = kde(sample).evaluate(x)
z = norm(-1, sigma).pdf(x) + norm(1, sigma).pdf(x)
z = z / np.trapz(z, x)
plt.plot(x, y, label="kde")
plt.plot(x, z, label="sampling distribution")
plt.hist(sample, normed=True, bins=100)
plt.legend()
plt.show()
