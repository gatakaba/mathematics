# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    return np.exp(-(x - 1) ** 2 - (y - 1) ** 2)

# 初期値セット
x, y = 0, 0

b = True
list = []
for i in range(10000):
    # ランダムに作成
    if b:
        dx = (np.random.random() - 0.5)
        dy = 0
    else:
        dx = 0
        dy = (np.random.random() - 0.5)
    # dx, dy = (np.random.random() - 0.5) , (np.random.random() - 0.5) 
    xs, ys = x + dx, y + dy
    if np.min([1, func(xs, ys) / func(x, y)]) > np.random.random():
        list.append([xs, ys])
        x, y = xs, ys
        b = not b
X = np.array(list)
X = X[len(X) / 2:]

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.plot(X[:, 0], X[:, 1])
plt.scatter(X[:, 0], X[:, 1])

plt.show()
