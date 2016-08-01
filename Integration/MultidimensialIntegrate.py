# -*- coding: utf-8 -*-

from scipy import integrate
import numpy as np

def uniIntegrate1():
    """
    1変数積分
    """
    y = lambda x: x ** 2
    ans, err = integrate.quad(y, 0, 4)[0]
    return ans

def uniIntegrate2():
    """
    1変数広義積分
    """
    y = lambda x:np.exp(-x ** 2)
    ans, err = integrate.quad(y, -np.inf, np.inf)[0]
    return ans

def doubleIntegrate():
    """
    2変数積分
    """
    f = lambda x, y:x + y
    ans, err = integrate.dblquad(f, np.pi, 2 * np.pi, lambda x: 0, lambda x: np.pi)
    return ans

def nDimIntegrate():
    """
    n変数積分
    w=f(x,y,z)=1/(1+x+y+z)^3
    ∫∫∫f(x,y,z) dxdydz
    V={(x,y,z)|x,y,z>0,x+y+z<1}
    """
    def func(x, y, z):
        return 1 / (1 + x + y + z) ** 3

    def lim0(x, y):
        # 0<1-y-x<1
        return [0, 1 - x - y]
    def lim1(x):
        # 0<1-y<x
        return [0, 1 - x]
    def lim2():
        # 0<x<1
        return [0, 1]
    ans, err = integrate.nquad(func, [lim0, lim1, lim2])
    return ans

print nDimIntegrate()
