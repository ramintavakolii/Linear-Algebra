import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# %matplotlib

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.array([1, 2, 3])
v = np.array([2.0, 0, -2])

rng = np.linspace(0, 1, 20)
rng2 = np.linspace(-0.5, 1.5, 20)
print(rng)
print(rng2)


for alpha in rng2:
    ax.cla()
    w = (1-alpha) * u + alpha * v

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    ax.quiver(0, 0, 0, w[0], w[1], w[2], color='b')
    ax.scatter(w[0], w[1], w[2], color='g')

    ax.quiver(0, 0, 0, u[0], u[1], u[2], color='r')
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='r')
    plt.draw()
    plt.pause(.1)

plt.show()

