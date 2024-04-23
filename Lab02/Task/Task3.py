import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

m, n = 20, 10
A = np.random.rand(m, n)
u = np.random.rand(n)

# print('A = ', A)
# print('u = ', u)

print('Shape of A = ',A.shape)
print('Shape of u = ',u.shape)

v = np.zeros(m)
print(v)
for i in range(n):
    v += A[:, i] * u[i]
    print(v)
print(v.shape, "\n")

# an equivalent program without loops in just a single line of code
v = np.dot(A, u)
print(v)
print(v.shape)
