import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

print('samping rate:', sampling_rate) 
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape 

print('signal length:', N)

channel0 = data[:,0]
channel1 = data[:,1]

scale = 2**np.linspace(-2,4, N)


print('shape_old:', scale.shape)
scale.shape = (N,1)
print('shape_new:', scale.shape)

data_new = np.int16(scale * data)
NN = data_new.shape[0]
print(data_new)
for i in range(int((NN/2)-1)):
    data_new[i], data_new[NN-1-i] = data_new[NN-i-1], data_new[i]
    print(data_new[i])
    data_new[NN-1-i]
    #if(i < 100):
    #    print(i, N-1-i)


# print(data)
print(data_new)
scipy.io.wavfile.write('output1.wav', sampling_rate, data_new)

