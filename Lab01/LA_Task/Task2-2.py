import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')
print('data shape:', data.shape)

N, no_channels = data.shape # signal length and no. of channels

scale = 2**np.linspace(-2,4, N)

scale.shape = (N,1)

data_new = np.int16(scale * data)

l1,l2 = data.shape
x = np.arange(0, l1, 1)

plt.plot(x,data_new)
plt.show()
