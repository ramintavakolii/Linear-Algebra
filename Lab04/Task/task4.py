import imageio
import matplotlib.pyplot as plt
import numpy as np

G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')

for alpha in np.linspace(0,1,20):
    J = I
    
    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()


