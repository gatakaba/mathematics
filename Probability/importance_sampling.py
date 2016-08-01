# coding:utf-8
# 重点サンプリング習作
# 提案分布の中からサンプリングを行い、特定の範囲から重点的にサンプリングを行う
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.integrate
gauss = norm(0, 1)
def Integrate():
    I = scipy.integrate.quad(gauss.pdf, 5, np.inf)[0]
    print "scipy.integrate\t\t", I

def NaiveMonteCalro():
    sample = gauss.rvs(size=10 ** 8)
    I = np.mean(map(lambda x:x > 5, sample))
    print "NaiveMonteCalro\t", I

def ImportanceSampling():
    proposed = norm(5 , 10)
    sample = proposed.rvs(size=100000)
    r = gauss.pdf(sample) / proposed.pdf(sample) * map(lambda x:x > 5, sample)
    I = np.mean(r)
    print "ImportanceSampling\t", I 
    
Integrate()
ImportanceSampling()
x = np.linspace(-5, 10, 1000)
y = gauss.pdf(x)
h = map(lambda x:x > 5, x)
plt.plot(x, y)
plt.plot(x, h)
plt.show()


