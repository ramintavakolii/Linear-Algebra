import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')
print('sampling rate:', sampling_rate)  # frequency (sample per second)
print('data type:', data.dtype)
print('data type:', type(data))
print('data shape:', data.shape)

N, no_channels = data.shape  # signal length and no. of channels

print('signal length or (N):', N)
print(data.shape[0])
channel0 = data[:, 0]
channel1 = data[:, 1]

data_1 = data[::-1]
print(data)
print(data_1)
print(data_1[0])
data_new = np.int16(data_1)

scipy.io.wavfile.write('output1.wav', sampling_rate, data_new)

