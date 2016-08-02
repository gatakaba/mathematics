"""
A model for coal mining disasters data with a changepoint
switchpoint ~ U(0, 110)
early_mean ~ Exp(1.)
late_mean ~ Exp(1.)
disasters[t] ~ Po(early_mean if t <= switchpoint, late_mean otherwise)
"""

import pymc3 as pm
import numpy as np
import matplotlib.pyplot as plt

# Time series of recorded coal mining disasters in the UK from 1851 to 1962
disasters_data = np.array([4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                           3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                           2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
                           1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                           0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                           3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                           0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

x = np.array(range(100)) / 10.0
years = len(disasters_data)


with pm.Model() as model:

    # Prior for distribution of switchpoint location
    switchpoint = pm.DiscreteUniform('switchpoint', lower=0, upper=years)
    # Priors for pre- and post-switch mean number of disasters
    early_mean = pm.Exponential('early_mean', lam=1.)
    late_mean = pm.Exponential('late_mean', lam=1.)

    # Allocate appropriate Poisson rates to years before and after current
    # switchpoint location
    idx = np.arange(years)

    rate = pm.switch(switchpoint >= idx, early_mean, late_mean)

    # Data likelihood
    disasters = pm.Poisson('disasters', rate, observed=disasters_data)


def run(n=1000):
    with model:
        # Initial values for stochastic nodes
        start = {'early_mean': 2., 'late_mean': 3.}
        tr = pm.sample(n, tune=500, start=start, njobs=-1)
    return tr

if __name__ == '__main__':
    tr = run()

    plt.subplot(211)
    plt.plot(range(years), disasters_data, "bo-")
    plt.subplot(212)
    for i in range(len(tr["early_mean"])):
        e = tr[early_mean][i]
        l = tr[late_mean][i]
        s = tr[switchpoint][i]
        v = [e if(y < s) else l for y in xrange(years)]
        plt.plot(range(years), v, alpha=0.03, c="blue")
    plt.figure(1)
    pm.traceplot(tr)
    plt.show()
