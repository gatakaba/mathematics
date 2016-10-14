import numpy as np
import matplotlib.pyplot as plt
# plot complex function

N = 300
# make scale
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
xx, yy = np.meshgrid(x, y)
z = xx + yy * 1.j

# complex function
w = np.log(np.sin(z))

# color mapping
# plt.pcolor(x, y, np.abs(w))
# countor line
plt.contour(x, y, np.abs(w))
plt.colorbar()
plt.show()

