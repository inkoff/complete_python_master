from array import array
from sys import argv
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)
print(array.shape)
array = np.zeros((3, 3), dtype=int)
print(array)
array = np.ones((3, 3), dtype=int)
print(array)
array = np.full((3, 3), 5, dtype=int)
print(array)
array = np.random.random((3, 3))
print(array)
print(array[0, 2])
print(array > 0.2)
print(array[array > 0.2])
print(np.sum(array > 0.5))
print(np.floor(array > 0.5))
inch = np.array([1, 2, 3])
cm = inch * 2.54
print(cm)
