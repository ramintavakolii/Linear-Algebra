import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, Face2, Face3, TargetFace2, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    
    plt.plot(X[:,0], X[:,1], 'o', color=color, markersize=3)

    for i,j in edges:
        xi = X[i,0]
        yi = X[i,1]
        xj = X[j,0]
        yj = X[j,1]
        
        # draw a line between X[i] and X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)
    plt.axis('square')
    plt.xlim(-100,100)
    plt.ylim(-100,100)

TargetFace = TargetFace2
NoisyTargetFace = TargetFace + 3 * np.random.randn(*TargetFace.shape)
    
face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = NoisyTargetFace.ravel();

F = np.stack((face1, face2, face3), axis=1)

for i in range(5):
    inds = np.random.choice(range(136), 3, replace=False)

    a1,b1,c1 = # solve 3 random equations
    a2,b2,c2 = # least squares solution
    
    Face_rnd = a1 * Face1 + b1 * Face2 + c1 * Face3
    Face_lsq = a2 * Face1 + b2 * Face2 + c2 * Face3

    plot_face(plt, NoisyTargetFace, edges, color='k')
    plot_face(plt, Face_rnd, edges, color='g')
    plot_face(plt, Face_lsq, edges, color='b')
    
    plt.show()

