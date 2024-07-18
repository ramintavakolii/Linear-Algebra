import numpy as np
import timeit

N = 100
P = 1000

# Return a sample (or samples) from the "standard normal" distribution.
A = np.random.randn(N, N)
# x = np.random.randn(N)
x = np.random.randn(N,P)
b = A @ x

print("Shape A=", A.shape)
print("Shape x=", x.shape)
print("Shape b=", b.shape)
# print("A=",A)
# print("x=",x)
# print("b=",b)

# solve for x given A and b
x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b

# One by one it reaches the power of 2 and then the radical
print("error1=", np.linalg.norm(x-x1))
print("error2=", np.linalg.norm(x-x2))

print("elapsed1=", timeit.timeit(lambda: np.linalg.solve(A, b), number=100))
print("elapsed2=", timeit.timeit(lambda: np.linalg.inv(A) @ b, number=100))
