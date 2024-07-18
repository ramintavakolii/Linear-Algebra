import numpy as np
import timeit

N = 100
x = np.random.randn(N)

# ----------------------------- non-singular case-----------------------------
A1 = np.random.randn(N, N)

b = A1 @ x
x1 = np.linalg.solve(A1, b)
x2 = np.linalg.inv(A1) @ b
print("----------------------")
print("error1 for non-singular=", np.linalg.norm(x-x1))
print("error2 for non-singular=", np.linalg.norm(x-x2))
print("----------------------")
print("elapsed1 for non-singular=",
      timeit.timeit(lambda: np.linalg.solve(A1, b), number=100))
print("elapsed2 for non-singular=",
      timeit.timeit(lambda: np.linalg.inv(A1) @ b, number=100))

# ----------------------------- near-singular case-----------------------------
A2 = np.random.randn(N, N)
A2[:, N-1] = A2[:, N-2]
A2 += 0.0001 * np.random.randn(N, N)

b = A2 @ x
x1 = np.linalg.solve(A2, b)
x2 = np.linalg.inv(A2) @ b
print("----------------------")
print("error1 for singular=", np.linalg.norm(x-x1))
print("error2 for singular=", np.linalg.norm(x-x2))
print("----------------------")
print("elapsed1 for singular=", timeit.timeit(
    lambda: np.linalg.solve(A2, b), number=100))
print("elapsed2 for singular=", timeit.timeit(
    lambda: np.linalg.inv(A2) @ b, number=100))
