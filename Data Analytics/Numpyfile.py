import numpy as np
file = np.genfromtxt('data.txt',delimiter=',',dtype='int16')
print(file)
print(file>6)
print(file[file>6])
print(np.any(file>3,axis=1))