import numpy as np
a= np.array([1,2,3])
b=a
b[0] = 100
print(b)
print(a)
a[0] = 1
b = a.copy()
print(b)
