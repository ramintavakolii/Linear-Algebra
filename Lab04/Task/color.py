import imageio
import matplotlib.pyplot as plt

I = imageio.imread('nasir-al-mulk.jpg')

print('I.shape=', I.shape)

plt.imshow(I)
plt.show()


