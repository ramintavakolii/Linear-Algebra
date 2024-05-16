import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# create a 3 x 2 matrix
A = np.array([[1, 2],
              [3, 4],
              [-2,1]])

fig = plt.figure()

# A 1 by 2 subplot grid, subplot 1 (3D)
ax1 = fig.add_subplot(1,2,2, projection='3d')
ax1.set_title('column space')


# ----------------Create Column Space--------------------

# creat a random column vector
u = np.random.randn(2,200)

# create a point in the column space of A
v = A @ u

ax1.scatter(v[0,:], v[1,:], v[2,:], color='b')
        

# A 1 by 2 subplot grid, subplot 2 (2D)
ax2 = fig.add_subplot(1,2,1)
ax2.set_title('row space')


# ----------------Create Row Space--------------------

# creat a random row vector
u = np.random.randn(200,3)

# create a point in the row space of A
v = u @ A

ax2.plot(v[:,0], v[:,1], 'ro')

plt.show()
