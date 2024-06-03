import imageio
import matplotlib.pyplot as plt
import numpy as np

G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')

print("G's Shape =",G.shape)
G = G.reshape((853,1280,1)) # for broadcasting
print("G's Shape =",G.shape)
print("I's Shape =",I.shape)
print('G = ',G)
print('I = ',I)

i=0
for alpha in np.linspace(0,1,20):
    
    J = I*alpha + G*(1-alpha) # Broadcasting
    # if (i==1):
    #     print('G2 = ',G*(1-alpha))
    #     print('I2 = ',I*alpha) 
    #     print('J = ',J) 
    #     i += 1q
        
    plt.imshow(J.astype(np.uint8), cmap='gray')
    plt.draw()
    plt.pause(.1)
    i += 1

plt.show()