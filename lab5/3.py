import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)


Z1 = X**0.25 + Y**0.25


Z2 = X**2 - Y**2


Z3 = 2*X + 3*Y


Z4 = X**2 - Y**2


Z5 = 2 + 2*X + 2*Y - X**2 - Y**2


fig = plt.figure(figsize=(6, 5))


ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title("z = x^0.25 + y^0.25")

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')
ax2.set_title("z = x² - y²")

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='coolwarm')
ax3.set_title("z = 2x + 3y")

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, Z5, cmap='magma')
ax4.set_title("z = 2 + 2x + 2y - x² - y²")

plt.tight_layout()
plt.show()
