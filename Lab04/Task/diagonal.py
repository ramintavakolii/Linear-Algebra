import numpy as np

D1 = np.diag([2,3,4])
D2 = np.diag([10,20,30,40])

print('D1=\n', D1)
print('D2=\n', D2)

A = np.array([[1,1,1,1],
              [1,2,2,2],
              [1,2,3,4]])

print('A=\n', A)
print('D1@A=\n', D1 @ A)

print('A@D2=\n', A @ D2)

              

