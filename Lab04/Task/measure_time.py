import numpy as np
import timeit

n = 1000

A = np.random.rand(n,n)

def f():
    np.linalg.inv(A)

t1 = timeit.timeit(f, number=1)
t2 = timeit.timeit(f, number=100)/100

print(t1)
print(t2)
