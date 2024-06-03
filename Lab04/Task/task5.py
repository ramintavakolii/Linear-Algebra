import imageio
import matplotlib.pyplot as plt
import numpy as np

G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')

G = G.reshape((853,1280,1)) # for broadcasting
# print('G = ',G)
# print('I = ',I)
print(G.shape)
print(I.shape)

for alpha in np.linspace(0,np.pi,20):

    l1 = [abs(np.sin(alpha)) ,abs(np.sin(alpha+np.pi/4)), abs(np.sin(alpha+np.pi/2))]
    s = np.array(l1)

    # I = I.astype(np.float64)
    # for i in range(3):
        # I[:,:,i] *= s[i]
    J = I * s
    print(I.dtype)
    print(s.dtype)
    print(J.dtype)  
    
    plt.imshow(J.astype(np.uint8), cmap='gray')
    plt.draw()
    plt.pause(.1)

plt.show()