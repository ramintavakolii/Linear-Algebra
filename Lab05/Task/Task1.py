import numpy as np
import timeit

N = 100
P = 1000
A = np.random.randn(N, N)
x = np.random.randn(N)
# x = np.random.randn(N,P)

noise = 0.001 * np.random.randn(N)

# ----------------------------- without noise-----------------------------

b = A @ x
x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b
print("error1 without noise=", np.linalg.norm(x-x1))
print("error2 without noise=", np.linalg.norm(x-x2))
print("----------------------")
# ----------------------------- 1*noise-----------------------------

b = A @ x + noise
x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b
print("error1 with noise=", np.linalg.norm(x-x1))
print("error2 with noise=", np.linalg.norm(x-x2))
print("----------------------")

# ----------------------------- 2*noise-----------------------------

b = A @ x + noise*2
x1 = np.linalg.solve(A, b)
x2 = np.linalg.inv(A) @ b
print("error1 with 2*noise=", np.linalg.norm(x-x1))
print("error2 with 2*noise=", np.linalg.norm(x-x2))
print("----------------------")
print("elapsed1 with 2*noise=",
      timeit.timeit(lambda: np.linalg.solve(A, b), number=100))
print("elapsed2 with 2*noise=",
      timeit.timeit(lambda: np.linalg.inv(A) @ b, number=100))
