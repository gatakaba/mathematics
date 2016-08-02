import numpy as np
import matplotlib.pyplot as plt
w = np.random.uniform(size=100)
w = w / np.sum(w)


# print np.random.choice(range(100), size=100, p=w)
for i in range(100):
    print np.random.choice(range(3), size=3, p=[0.8, 0.1, 0.1])
