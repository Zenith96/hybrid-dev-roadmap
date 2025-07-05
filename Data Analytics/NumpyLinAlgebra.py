import numpy as np
a= np.ones((2,3),dtype='int16')
print(a)
b = np.ones((3,2),dtype = 'int16')
print(b)
print(np.matmul(a,b))
c = np.identity(3)
print(np.linalg.det(c))