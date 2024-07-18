import numpy as np
import timeit

N = 100
P = 1000
A = np.random.randn(N, N)
x = np.random.randn(N)
# x = np.random.randn(N,P)

# print("A=",A)
A[:, N-1] = A[:, N-2]
# print("A=",A)

noise = 0.001 * np.random.randn(N)

# ----------------------------- singular-----------------------------

b = A @ x
x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b
print("----------------------")
print("error1 for singular=", np.linalg.norm(x-x1))
print("error2 for singular=", np.linalg.norm(x-x2))
print("----------------------")
print("elapsed1 for singular=", timeit.timeit(
    lambda: np.linalg.solve(A, b), number=100))
print("elapsed2 for singular=", timeit.timeit(
    lambda: np.linalg.inv(A) @ b, number=100))
