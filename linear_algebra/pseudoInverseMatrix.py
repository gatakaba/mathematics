# coding:utf-8
# http://d.hatena.ne.jp/Zellij/20120811/p1
import numpy as np
import matplotlib.pyplot as plt

def dim1():
    # 線の中点かつ距離が最も0に近い点
    A = np.array([[1, 1], [1, 1]])
    y = np.array([4, 0])
    x = np.dot(np.linalg.pinv(A), y)
    print x

    scaleX = np.linspace(-2, 6)
    scaleY1 = (-A[0, 0] * scaleX + y[0]) / A[0, 1]
    scaleY2 = (-A[1, 0] * scaleX + y[1]) / A[1, 1]

    plt.plot(scaleX, scaleY1)
    plt.plot(scaleX, scaleY2)
    plt.scatter(x[0], x[1])
    plt.show()

def dim2():
    # 通常の解法で解ける
    A = np.array([[1, 1], [1, -1]])
    y = np.array([4, 0])
    x = np.dot(np.linalg.pinv(A), y)
    print x

    scaleX = np.linspace(-2, 6)
    scaleY1 = (-A[0, 0] * scaleX + y[0]) / A[0, 1]
    scaleY2 = (-A[1, 0] * scaleX + y[1]) / A[1, 1]

    plt.plot(scaleX, scaleY1)
    plt.plot(scaleX, scaleY2)
    plt.scatter(x[0], x[1])
    plt.show()

def dim3():
    # ランクが多すぎる場合
    # すべての線からの等距離
    A = np.array([[1, 1], [1, -1], [0, 1]])
    y = np.array([4, 0, 1])
    x = np.dot(np.linalg.pinv(A), y)
    print x

    scaleX = np.linspace(-2, 6)
    scaleY1 = (-A[0, 0] * scaleX + y[0]) / A[0, 1]
    scaleY2 = (-A[1, 0] * scaleX + y[1]) / A[1, 1]
    scaleY3 = (-A[2, 0] * scaleX + y[2]) / A[2, 1]
    plt.plot(scaleX, scaleY1)
    plt.plot(scaleX, scaleY2)
    plt.plot(scaleX, scaleY3)
    plt.scatter(x[0], x[1])
    plt.show()
dim1()
