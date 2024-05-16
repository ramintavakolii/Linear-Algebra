import numpy as np
import timeit

n = 1000

A = np.random.rand(n,n)

t1 = timeit.timeit(lambda : np.linalg.inv(A), number=1)
t2 = timeit.timeit(lambda : np.linalg.inv(A), number=100)/100

print(t1)
print(t2)
