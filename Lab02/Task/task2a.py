import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, Face2, Face3, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    
    plt.plot(X[:,0], X[:,1], 'o', color=color)

    for t in range(len(edges)):
        i,j = edges[t]  # edge from node i to node j

        xi = X[i,0]
        yi = X[i,1]

        xj = X[j,0]
        yj = X[j,1]
            
        # draw a line between X[i] and X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)

    plt.axis('square') 
    plt.xlim(-100,100)
    plt.ylim(-100,100)

print("some edges:",edges[0],edges[1])  # The list edge contains a list of edges

rng1 = np.linspace(0,1,20)
rng2 = np.linspace(-0.5,1.5,20)

l_face = [Face1,Face2,Face3,Face1]

for F in range(3):
    for alpha in rng1:

        plt.cla()

        face =(1-alpha) * l_face[F]  + alpha * l_face[F+1]

        plot_face(plt, face, edges, color='b')
        plt.draw()
        plt.pause(.1)

    plt.draw()
    plt.pause(0.5) 

plt.show()