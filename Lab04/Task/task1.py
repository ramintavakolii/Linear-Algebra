import numpy as np
import timeit

A = np.random.rand(100,200)
d1 = np.random.rand(1,100).reshape((100,1))
D1 = np.diag(d1.ravel()) # we have a diagonal matrices

# print('d1=\n', d1)
# print('A=\n', A)


print((d1.ravel()).shape)
print(D1.shape)
# print('D1=\n', D1)

t1 = timeit.timeit(lambda : d1*A, number=1000)/1000
t2 = timeit.timeit(lambda : D1@A, number=1000)/1000

print("t1 = ",t1)
print("t2 = ",t2)

print('d1.shape=\n', d1.shape)
print('A.shape=\n', A.shape)
# print('d1 * A=\n', d1 * A)
print('d1*A.shape=\n', (d1*A).shape)
# print('D1 * A=\n', D1 @ A)
print('D1@A.shape=\n', (D1@A).shape)
print((D1@A)==(d1*A))