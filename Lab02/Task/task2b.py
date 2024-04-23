import matplotlib.pyplot as plt
import numpy as np
import random

from face_data import Face1, Face2, Face3, TargetFace1, TargetFace2, edges


def plot_face(plt, X, edges, color='b'):
    "plots a face"

    plt.plot(X[:, 0], X[:, 1], 'o', color=color)

    i, j = edges[0]  # edge from node i to node j
    xi = X[i, 0]
    yi = X[i, 1]

    xj = X[j, 0]
    yj = X[j, 1]

    # draw a line between X[i] and X[j]
    plt.plot((xi, xj), (yi, yj), '-', color=color)

    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)


# ----------------------------------------------------- make a guess ----------------------------------------------------------------
a = 0.65
b = 0.65
c = -0.3

# ----------------------------------------- find the scalars without trial and error -----------------------------------------------
for i in range(10000000):

    a = round(np.random.rand(), 5)
    b = round(np.random.rand(), 5)
    c = round(np.random.rand(), 5)
    # c = 1 - (a + b)

    # if (c < 0 or c < 0.5 or c > 0.65):
    #     continue

    # print(i, a, b, c)
    F = a * Face1 + b * Face2 + c * Face3
    # print(F == TargetFace1)
    t = sum(np.round(F, 1) == TargetFace2)

    # change a,b,c until the two plots align
    if (t[1] >= 15 and t[0] >= 15):

        print('iteration = ', i)
        print('a, b, c = ', a, b, c)
        print('number of point align = ', t)
        print(sum(t))

        plot_face(plt, TargetFace2, edges, color='r')
        plot_face(plt, F, edges, color='g')
        break
plt.show()

# ----------------------------------------- linear (not necessarily convex) combination -------------------------------------------
# a = 0.3
# b = 0.5
# c = 0.4

# F2 = a * Face1 + b * Face2 + c * Face3
# plot_face(plt, TargetFace2, edges, color='y')
# plot_face(plt, F2, edges, color='g')

plt.show()
