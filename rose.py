# r = cos(n*theta) expressed as a parametric equation.
# That is, x = cos(ntheta)cos(theta) and y = cos(ntheata)sin(theta)


import numpy as np
import matplotlib.pyplot as plt

n = (4/5)
theta = np.arange(0, 50, 0.1)
x = np.cos(n * theta) * np.cos(theta)
y = np.cos(n * theta) * np.sin(theta)


plt.axis('off')


plt.plot(x,y, linewidth=2)
plt.show()