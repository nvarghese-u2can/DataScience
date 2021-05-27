import numpy as np
import random
arr = np.array([1, 2, 3])
arr1 = np.arange(0, 11)
print(arr)
print(arr.shape)
print('\n')
print(arr1)
print(arr1[1:10])
print(arr1[::])
print('\n')

allZ = np.zeros(5)
print(allZ)
print('\n')
print(allZ.dtype)
print('\n')

allO = np.ones((5, 5))
print(allO)
print(allO.shape)

print('\n')
print(allO.dtype)
print('\n')

allE = np.eye(5, 5)
print(allE)
print('\n')
print(allE.dtype)
print('\n')

arr2 = np.arange(0, 25).reshape(5, 5)
print(arr2)
print('\n')
print(arr2[:2, 2:])

arr3 = np.arange(0, 15)
print(arr3)
arr4 = arr3.copy()
arr4[:] = 100
print(arr4)

arr5 = arr3
arr5[:5] = 250

print(arr3)

print('\n')

arr6 = np.arange(0, 25)
print([arr6 < 5])
print(arr6[arr6 < 5])

