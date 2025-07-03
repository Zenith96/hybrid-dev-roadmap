import numpy as np
arr = np.ones((5,5),dtype='int16')
z = np.full((3,3),0)
z[1][1] = 9
arr[1:4,1:4]= z
print(arr)
