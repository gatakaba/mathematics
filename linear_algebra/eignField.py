
# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 2d matrix positive define matrix filed
N = 100
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)
z = np.linspace(-10, 10, N)

xx, yy, zz = np.meshgrid(x, y, z)
w1 = (xx + zz) + ((xx - zz) ** 2 + 4 * yy ** 2) ** 0.5
w2 = (xx + zz) - ((xx - zz) ** 2 + 4 * yy ** 2) ** 0.5
w = (np.sign(w1) + 1) * (np.sign(w2) + 1)

X = np.c_[np.ravel(xx), np.ravel(yy), np.ravel(zz)]
X += np.random.normal(size=X.shape)


index1 = np.where(np.ravel(w) == 0)
index2 = np.where(np.ravel(w) == 4)

import sys
# sys.exit()
from mayavi import mlab
# blue field means negative
mlab.points3d(X[index1, 0], X[index1, 1], X[index1, 2], color=(0, 0, 1), mode="point")
# red field means positive
mlab.points3d(X[index2, 0], X[index2, 1], X[index2, 2], color=(1, 0, 0), mode="point")
mlab.show()

