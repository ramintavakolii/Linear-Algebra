import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice2.wav')

print('data shape:', data.shape)

N, no_channels = data.shape # signal length and no. of channels

scale = 2**np.linspace(-2,4, N)
scale.shape = (N,1)
data_new = np.int16(scale * data)

l1,l2 = data.shape
print(l1,l2)
x = np.arange(0, l1, 1)
y1 = data[:,0]
y2 = data[:,1]
print('x = ',x)
print('y1 = ',y1)
print('y2 = ',y2)

print('x shape: ',x.shape)
print('y1 shape: ',y1.shape,'y2 shape: ',y2.shape)


# Set the figure size using figsize
figure, axis = plt.subplots(2, 2,figsize=(12, 8),) 



axis[0][0].plot(x, y1 ,label='channel_1') 
axis[0][0].plot(x, y2,label='channel_2') 
axis[0][0].legend() 
axis[0][0].set_title("two channels together in the\n same axes", color='blue')

axis[0][1].plot(x, data,label=['channel_1','channel_2'])
axis[0][1].legend() 
axis[0][1].set_title("data as the second argument", color='blue')

axis[1][0].plot(x, data_new,label=['channel_1','channel_2'])
axis[1][0].legend() 
axis[1][0].set_title("output data", color='blue')

# Remove the undesired subplot (top-right)
figure.delaxes(axis[1, 1])

# Adjust layout to prevent clipping of titles
plt.tight_layout()


plt.show()
