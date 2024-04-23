import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, Face2, Face3, edges
import random

# print(type(edges))

def plot_face(plt, face, edges, color='b'):
    "plots a face"

    plt.plot(face[:, 0], face[:, 1], 'o', color=color)

    i, j = edges[0]  # edge from node i to node j
    
    xi = face[i, 0]
    yi = face[i, 1]
    xj = face[j, 0]
    yj = face[j, 1]

    # draw a line between X[i] and X[j]
    plt.plot((xi, xj), (yi, yj), '-', color=color)

    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)


# plot_face(plt, Face1, edges, color='b')
# plt.show()
