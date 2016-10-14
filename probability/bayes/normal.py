# coding:utf-8
# 正規分布のベイズ推定
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm

y = np.random.normal(10, 1, size=10000)
niter = 10000


with pm.Model() as model:
    # prior distribution
    mu = pm.Normal('mu', mu=0, sd=10)
    sigma = pm.HalfNormal('sigma', sd=1)
    # model likelihood
    y_obs = pm.Normal('y_obs', mu=mu, sd=sigma, observed=y)
    step = pm.Metropolis()
    trace = pm.sample(niter, step)


pm.traceplot(trace)
plt.show()
