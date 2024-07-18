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


# make a guess
a = 1/3.
b = 1/3.
c = 1/3.

face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = TargetFace2.ravel()

print("-----------------------------")
print("Shape t=", t.shape)
print("Shape Face1=", Face1.shape)
print("Shape Face2=", Face2.shape)
print("Shape Face3=", Face3.shape)
print("-----------------------------")
print("Shape Face1=", face1.shape)
print("Shape Face2=", face2.shape)
print("Shape Face3=", face3.shape)
print("Shape t=", t.shape)
print("-----------------------------")

F = np.stack((face1, face2, face3), axis=1)
print("Shape F=", F.shape)


Face = a * Face1 + b * Face2 + c * Face3


plot_face(plt, TargetFace2, edges, color='r')
plot_face(plt, Face, edges, color='g')

# change a,b,c until the two plots align

plt.show()
