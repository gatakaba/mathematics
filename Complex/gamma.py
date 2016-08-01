import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
# plot complex function

N = 300
# make scale
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
xx, yy = np.meshgrid(x, y)
z = xx + yy * 1.0j

# complex function
w = np.abs(gamma(z))
w[np.where(w > 10)] = 10
from mayavi import mlab

mlab.barchart(xx, yy, w)
mlab.show()
# color mapping
plt.pcolor(x, y, np.abs(w))
# countor line
# plt.contour(x, y, np.abs(w))
plt.colorbar()
plt.show()

