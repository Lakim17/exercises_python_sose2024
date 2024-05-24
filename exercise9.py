
import numpy as np

M = np.eye(5, dtype=int)

M[3:5,0:2] = 2
M[0:2,3:5] = 3

print(M)


# vorherige aufgabe

a = np.arange(1,13)
a_3d = a.reshape(2,3,2) 

print(a_3d) 
print(a_3d.ndim) 
print(a_3d.shape) 
print(a_3d.size) 
print(a_3d.dtype) 

