import numpy as np
import matplotlib.pyplot as plt

n = 11

S1 = np.vstack((-np.cos(np.linspace(0, np.pi, n)),
                -.7+np.sin(np.linspace(0, np.pi, n)))).T

print(S1)
S2 = np.vstack((np.linspace(-1.2, 1.2, n),
                np.zeros(n))).T
print(S2)

''''
s1 = S1.ravel()
s2 = S2.ravel()
print(s2)
s3 = 0.5 * s1 + 0.5 * s2
S3 = s3.reshape((n,2))
'''

S3 = 0.5 * S1 + 0.5 * S2

print(S1.shape)
print(S2.shape)
print(S3.shape)

plt.plot(S1[:, 0], S1[:, 1], 'bo-')
plt.plot(S2[:, 0], S2[:, 1], 'ro-')
plt.plot(S3[:, 0], S3[:, 1], 'go-')

plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()