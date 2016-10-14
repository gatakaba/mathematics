import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg


def test1():
    A = np.array([[1, 0, 0], [0, 1, 1]])
    u, s, v = linalg.svd(A)
    print u
    print s
    print v

def SVDIris():
    from sklearn.datasets import load_iris
    iris = load_iris()
    data = iris.data
    u, s, v = linalg.svd(data)
    print v
    print s

def SVDRandom():
    myu = [0, 0]
    sigma = [[1, 3], [3, 10]]
    N = 900
    # X = np.random.multivariate_normal(myu, sigma, N)
    myu1 = [0, 0]
    sigma1 = [[1, 0], [0, 1]]
    myu2 = [5, 5]
    sigma2 = [[1, 0], [0, 1]]
    myu3 = [-5, 5]
    sigma3 = [[1, 0], [0, 1]]

    X1 = np.random.multivariate_normal(myu1, sigma1, N / 3)
    X2 = np.random.multivariate_normal(myu2, sigma2, N / 3)
    X3 = np.random.multivariate_normal(myu3, sigma3, N / 3)


    X = np.r_[X1, X2, X3]
    u, s, v = np.linalg.svd(X)
    sigma = np.zeros([N, 2])

    sigma[0, 0] = s[0]
    sigma[1, 1] = s[1]
    Xdash = np.dot(np.dot(u, sigma), v)

    Xdash = np.dot(u[:, 0][None].T, v[:, 0][None]) * s[0]

    fig = plt.figure(1)
    plt.scatter(X[:, 0], X[:, 1])
    plt.scatter(Xdash[:, 0], Xdash[:, 1], c="red", alpha=0.5)
    # plt.axis("equal")
    # np.testing.assert_almost_equal(Xdash, X)
    # fig = plt.figure(2)
    # plt.imshow(u)
    plt.show()

def SVDRandom2():
    myu1 = [0, 0]
    sigma1 = [[1, 0], [0, 1]]
    myu2 = [5, 5]
    sigma2 = [[1, 0], [0, 1]]

    N = 1000
    X1 = np.random.multivariate_normal(myu1, sigma1, N / 2)
    X2 = np.random.multivariate_normal(myu2, sigma2, N / 2)
    X = np.r_[X1, X2]
    print X.shape
    u, s, v = np.linalg.svd(X)
    sigma = np.zeros([N, 2])

    plt.imshow(u)
    plt.colorbar()
    plt.show()
    sigma[0, 0] = s[0]
    sigma[1, 1] = s[1]
    Xdash = np.dot(np.dot(u, sigma), v)
    print np.dot(X.T, X)
    fig = plt.figure(1)
    plt.scatter(X[:, 0], X[:, 1])
    plt.axis("equal")
    np.testing.assert_almost_equal(Xdash, X)
    # fig = plt.figure(2)
    # plt.imshow(u)
    plt.show()

A = np.array([[2, 3], [2, 2]])


