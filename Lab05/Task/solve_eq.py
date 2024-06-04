import numpy as np
import timeit

N = 100

A = np.random.randn(N,N)
x = np.random.randn(N)
b = A @ x

# solve for x given A and b
x1 = np.linalg.solve(A,b)
x2 = np.linalg.inv(A) @ b

print("error1=", np.linalg.norm(x-x1))
print("error2=", np.linalg.norm(x-x2))

print("elapsed1=", timeit.timeit(lambda : np.linalg.solve(A,b), number=100))
print("elapsed2=", timeit.timeit(lambda : np.linalg.inv(A) @ b, number=100))




