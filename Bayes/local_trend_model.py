# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm

np.random.seed(0)
N = 10
state = 0
x, z = [], []
niter = 100000

for i in range(N):
    x.append(np.random.normal(state, 1))
    z.append(state)
    state = np.random.normal(state, 0.1)
x = np.array(x)
z = np.array(z)

with pm.Model() as model:
    s1 = pm.HalfNormal("sigma_state", sd=10)
    s2 = pm.HalfNormal("sigma_observed", sd=10)
    # model
    states = [pm.Normal("s0", mu=0, sd=s1)]
    for i in range(1, N):
        states.append(
            pm.Normal(name="s" + str(i), mu=states[-1], sd=s1))
    # likelihood
    obs = pm.Normal("obs", mu=states, sd=s2, observed=x)
    step = pm.Metropolis()
    trace = pm.sample(niter, step)


def calc_expectation(samples):
    N = 10000
    samples = samples[len(samples) / 2:]
    p, bins = np.histogram(samples, bins=N, density=True)
    x = np.linspace(np.min(bins), np.max(bins), N)
    return np.dot(p, x) / N


print calc_expectation(trace["sigma_state"])
print calc_expectation(trace["sigma_observed"])
mu = []
for i in range(N):
    mu.append(calc_expectation(trace["s" + str(i)]))
plt.plot(mu)
plt.plot(z)
plt.show()
