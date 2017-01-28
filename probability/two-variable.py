# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
x ~ N(m1,1)
y ~ N(m2,1)
として、z=x*yの確率密度関数を求める
"""
N = 100
u = np.linspace(0.1, 10, 100)
v = np.linspace(-5, 5, N)
uu, vv = np.meshgrid(u, v)
m1, m2 = 2.5, 1.5
sigma = 1.0
Puv = np.exp(-(vv - m1) ** 2 / (2 * sigma)) * np.exp(-(uu / vv - m2) ** 2 / (2 * sigma)) 
plt.figure(0)
plt.pcolor(uu, vv, Puv)
plt.figure(1)


plt.plot(u , np.sum(Puv, axis=0))
plt.show()

