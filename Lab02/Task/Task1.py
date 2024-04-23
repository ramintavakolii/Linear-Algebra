import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 11

S1_1 = np.vstack((-np.cos(np.linspace(0, np.pi, n)), -.7 +
                 np.sin(np.linspace(0, np.pi, n)))).T
S1_2 = np.vstack((np.cos(np.linspace(0, np.pi, n)), -.7 +
                 np.sin(np.linspace(0, np.pi, n)))).T

S2 = np.vstack((np.linspace(-1.2, 1.2, n), np.zeros(n))).T

# print(S1_1)
# print(S1_2)

print(S1_1.shape)
print(S2.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rng1 = np.linspace(0, 1, 20)
rng2 = np.linspace(0, 1.5, 20)
rng3 = np.linspace(-2, 2, 20)

# Shape morphing
for alpha in rng3:

    plt.cla()

    S3 = (1-alpha) * S1_1 + alpha * S2

    plt.plot(S1_1[:, 0], S1_1[:, 1], 'bo-')
    plt.plot(S2[:, 0], S2[:, 1], 'ro-')
    plt.plot(S3[:, 0], S3[:, 1], 'go-')

    plt.axis('equal')

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    plt.draw()
    plt.pause(.2)

plt.show()
