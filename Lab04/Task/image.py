import imageio
import matplotlib.pyplot as plt

I = imageio.imread('nasir-al-mulk-gray.jpg')

print('I=\n', I)
print('I.dtype=\n', I.dtype)
print('I.shape=\n', I.shape)

plt.imshow(I, cmap='gray')
plt.show()

plt.imshow(I.T, cmap='gray')
plt.show()

plt.imshow(I[100:400, 300:600], cmap='gray')
plt.show()



