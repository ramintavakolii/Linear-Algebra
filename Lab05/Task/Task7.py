import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, Face2, Face3, TargetFace2, edges


def plot_face(plt, X, edges, color='b'):
    "plots a face"

    plt.plot(X[:, 0], X[:, 1], 'o', color=color, markersize=3)

    for i, j in edges:
        xi = X[i, 0]
        yi = X[i, 1]
        xj = X[j, 0]
        yj = X[j, 1]

        # draw a line between X[i] and X[j]
        plt.plot((xi, xj), (yi, yj), '-', color=color)
    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)


TargetFace2 += 1 * np.random.randn(*TargetFace2.shape)

face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = TargetFace2.ravel()

F = np.stack((face1, face2, face3), axis=1)


for i in range(5):
    inds = np.random.choice(range(136), 3, replace=False)
    print('inds =', inds)
    # choose the equations
    f = F[inds, 0:3]
    T = t[inds]

    a, b, c = np.linalg.solve(f, T)

    Face = a * Face1 + b * Face2 + c * Face3

    plot_face(plt, TargetFace2, edges, color='r')
    plot_face(plt, Face, edges, color='g')

    plt.show()
