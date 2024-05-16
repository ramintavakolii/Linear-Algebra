import numpy as np

m,n,p = 100,50, 2000

A = np.random.rand(m,n,p) 
s = np.random.rand(p)

for i in range(p):
    A[:,:,i] *= s[i]


