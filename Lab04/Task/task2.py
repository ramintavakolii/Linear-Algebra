import numpy as np
import timeit

m,n,p = 2,1, 20

A = np.random.rand(m,n,p) 
s = np.random.rand(p)

print('A=\n', A) 
print('Shape of A=\n', A.shape)
print('Shape of s=\n', s.shape)

# B = A*s

def f():
    for i in range(p):
        A[:,:,i] *= s[i] # it is deep copy
    print(A)

f()
# print(B==A)

def g():
    A*s
print(s*A)

# t1 = timeit.timeit(f , number=100)/100
# t2 = timeit.timeit(g, number=100)/100

# print("t1 = ",t1)
# print("t2 = ",t2)

