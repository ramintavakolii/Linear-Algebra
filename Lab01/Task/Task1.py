import numpy as np

# Consider an arbitrary A matrix like
A = np.random.rand(200,10)
print(A.shape[0])


# print(A.shape[1]) = 10

mu = np.zeros(A.shape[1])
print(mu.shape)
for i in range(A.shape[0]):
    mu += A[i]
print(mu.shape)
mu /= A.shape[0]

B = np.zeros_like(A)

for i in range(A.shape[0]):
    B[i] = A[i] - mu
print('B = ',B, '\n')

# equivalent program 1
for i in range(A.shape[0]):
    B[i] = A[i] - (A.mean(axis=0))
# print(B,'\n')

# equivalent program 2
B = A - A.mean(axis=0)
print('B = ',B,'\n')


# TODO: equivalent program 1, Calculate B
# TODO: equivalent program 2, Calculate B