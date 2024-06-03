import imageio
import numpy as np
import matplotlib.pyplot as plt

I = imageio.imread('nasir-al-mulk-gray.jpg')

print('I=\n', I)
print('I.shape=\n', I.shape)

print('I.dtype=\n', I.dtype)
print('I.shape=\n', I.shape)

plt.imshow(np.hstack(((np.vstack((I, I[::-1]))),(np.vstack((I, I[::-1]))))), cmap='gray')
plt.show()

