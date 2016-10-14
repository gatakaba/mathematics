import numpy as np
from statsmodels.tsa import arima_model
import matplotlib.pyplot as plt

N = 400
M = N / 2

data = np.cumsum(np.random.normal(size=N)) + range(N)


results = arima_model.ARIMA(data[:M], order=[1, 1, 3]).fit()


plt.plot(data)
plt.plot(results.predict(start=10, end=N))
plt.show()



