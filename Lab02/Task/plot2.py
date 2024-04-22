import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# plot multiple points
u = np.array([1, 2, 3])
v = np.array([2, 0, -2])
w = np.array([-1, -1, -1])

xs = [u[0], v[0], w[0]]
ys = [u[1], v[1], w[1]]
zs = [u[2], v[2], w[2]]

# base of the vectors set to the origin
tail_x = [0, 0, 0]
tail_y = [0, 0, 0]
tail_z = [0, 0, 0]

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

ax.quiver(tail_x, tail_y, tail_z, xs, ys, zs, color='r')
plt.show()
