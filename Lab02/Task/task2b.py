import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, Face2, Face3, TargetFace1, TargetFace2, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    
    plt.plot(X[:,0], X[:,1], 'o', color=color)

    i,j = edges[0]  # edge from node i to node j
    xi = X[i,0]
    yi = X[i,1]

    xj = X[j,0]
    yj = X[j,1]
        
    # draw a line between X[i] and X[j]
    plt.plot((xi,xj), (yi,yj), '-', color=color)

    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    

# make a guess
a = 1/3.
b = 1/3.
c = 1/3.

F = a * Face1 + b * Face2 + c * Face3

plot_face(plt, TargetFace1, edges, color='r')
plot_face(plt, F, edges, color='g')

# change a,b,c until the two plots align

plt.show()





    
    

