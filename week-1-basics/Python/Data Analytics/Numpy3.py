import numpy as np
before  = np.array([[1,2,3],[4,5,6]])
after = before.reshape(3,2)
print(before)
print(after)
v1 =np.array([1,2,3,4])
v2 =np.array([23,4,6,6])
print(np.vstack([v1,v2]))
print(np.hstack((v1,v2)))