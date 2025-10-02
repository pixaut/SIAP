import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Диапазон значений x и y
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

# Функции
Z1 = X**0.25 + 0.25
Z2 = X**2 - Y**2
Z3 = 2*X + 3*Y
Z4 = 2 + 2*X + 2*Y - X**2 - Y**2

# Список функций и названий
functions = [(Z1, "z = x^0.25 + 0.25"),
             (Z2, "z = x^2 - y^2"),
             (Z3, "z = 2x + 3y"),
             (Z4, "z = 2 + 2x + 2y - x^2 - y^2")]

# Построение графиков
fig = plt.figure(figsize=(12, 8))

for i, (Z, title) in enumerate(functions, 1):
    ax = fig.add_subplot(2, 2, i, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

plt.tight_layout()
plt.show()
