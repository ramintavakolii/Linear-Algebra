import numpy as np


x_true = np.array([3, 1.5, -1.0, 2.4, -3, -.1, 2.2, 4.1, -3.2, 1.0])

n = x_true.size  # no. of unknowns

m = 2000  # no of equations (measurements)
A = np.random.randn(m, n)
print(A.dtype)

# create the measurments
y_true = A @ x_true
# print("y_true:",y_true)

# add noise to the measurments
x_e = 0
Error_sum = 0
for i in range(100):

    sigma = 0.01
    measurement_noise = sigma * np.random.randn(m)
    y_noisy = y_true + measurement_noise

    # we have access to the matrix "A" and noisy measurements "y_noisy".
    # Frome these, we intend to estimate "x_true" using least squares
    x_est = np.linalg.inv(A.T@A) @ A.T @ y_noisy
    # x_est = np.linalg.solve(A.T@A, A.T @ y_noisy)
    # x_est = np.linalg.lstsq(A,y_noisy)[0]
    Error_sum += np.linalg.norm(x_est - x_true)

    # measure the distance between the estimated unkowns "x_est"
    # and the ture ones "x_true"
Error_sum = Error_sum/100
print('error=', Error_sum)


