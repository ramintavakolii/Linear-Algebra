import matplotlib.pyplot as plt
import numpy as np

from face_data import Face1, edges

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    plt.plot(X[:,0], X[:,1], 'o', color=color)

    for i,j in edges:
        xi,yi = X[i]
        xj,yj = X[j]
        
        plt.plot((xi,xj), (yi,yj), '-', color=color)
        
        plt.axis('square')
        plt.xlim(-100,100)
        plt.ylim(-100,100)


th = np.pi/6
A = np.array([[np.cos(th), np.sin(th)],
              [-np.sin(th), np.cos(th)]])
        
X = Face1 @ A
        
plot_face(plt, X, edges, color='b')
plt.show()



