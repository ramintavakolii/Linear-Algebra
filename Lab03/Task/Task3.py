import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# create a 3 x 2 matrix
A = np.array([[1, 2, 1],
              [2, -1, -1],
              [-1, 1, -2]])
B = np.array([[1, 2, -3],
              [3, 1, 1],
              [2, 1, 0]])
C = np.array([[1, 2, -3],
              [3, 6, -9],
              [-2, -4, 6]])


fig = plt.figure(figsize=(10,7))

# ---------------- Create Column Space Of Matrix --------------------
def C_Space(Number_M, Matrix, name, c):
    ax1 = fig.add_subplot(2, 3, Number_M, projection='3d')
    ax1.set_title("Column and Row space %s"%name)

    u = np.random.randn(3,200)

    v = Matrix @ u
    ax1.scatter(v[0,:], v[1,:], v[2,:], color=c)
    return ax1
    

# ---------------- Create Row Space Of Matrix --------------------

def R_Space(Number_M, Matrix, name, c,ax1):

    # ax1 = fig.add_subplot(2,3,Number_M,projection='3d')
    # ax1.set_title('row space %s'%name)

    u = np.random.randn(200,3)

    v = u @ Matrix

    ax1.scatter(v[:,0], v[:,1], v[:,2], color=c)



ax1 = C_Space(1,A,'A','b')
ax2 = C_Space(2,B,'B','b')
ax3 = C_Space(3,C,'C','b')

R_Space(1,A,'A','r',ax1)
R_Space(2,B,'B','r',ax2)
R_Space(3,C,'C','r',ax3)

plt.show()
