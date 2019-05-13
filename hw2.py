import numpy as np
data = np.loadtxt("bb.data",delimiter="::",dtype = str)
dat = np.array(data)
a = np.zeros((569,10))
for i in range(10):
    a[i] = dat[i].split(',')
print(a)   