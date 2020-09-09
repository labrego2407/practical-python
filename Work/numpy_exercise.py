# numpy_exercise.py
#
# File to practice numpy arrays
import os
os.system('cls')
#-----------------------------------------
import numpy as np

a = np.array([1, 2, 3])
a2 = np.array([1, 2, 3], dtype='int16') #can specify the type
# print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# Get dimension
# print(a.ndim)

# Get shape
# print(a.shape)

# Get type
# print(a.dtype)
# print(a2.dtype)

# Get size
# print(a.itemsize)
# print(a2.size)

a = np.array([[1, 2, 3, 4, 5, 6 ,7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)

#get a specific element [row, column]
# print(a[1, 5])

#3d array
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
# print(b)
#get specific element (work outside in)
# print(b[0])
# print(b[0, 1])
# print(b[0, 1, 1])

output = np.ones((5, 5))
# print(output)

z = np.zeros((3, 3))
z[1, 1] = 9
# print(z)

output[1:-1, 1:-1] = z
# print(output)

a = np.array([0, 1, 2])
np.tile(a, 2)
# array([0, 1, 2, 0, 1, 2])

np.tile(a, (2, 2))
# array([
#        [0, 1, 2, 0, 1, 2],
#        [0, 1, 2, 0, 1, 2]
#       ])
b = np.tile(a, (2, 1, 2))
# print(b.shape)
# print(np.tile(a, (2, 1, 2)))
# array([
#        [[0, 1, 2, 0, 1, 2]],
#        [[0, 1, 2, 0, 1, 2]]
#       ])

# Vertical stack of arrays
array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])

# two arrays
output = np.vstack([array1, array2])
# print(output)

# can repeat any or all of the arrays N times in any order
output = np.vstack([array1, array2, array1, array2, array2])
# print(output)

array3 = np.array([9,10,11,12.])
output = np.vstack([array1, array2, array1, array2, array3])
# print(output)

a = np.arange(9).reshape((3, 3))
# print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
output = np.where(a<4)
# print(output)

test = np.array([1,13,21,11,196,75,4,3,34,6,7,8,0,1,2,3,4,5])
# a = np.where(test > 50)
# print(a)

a = np.where(test > 50, test, 0)
# print(a)


output = np.genfromtxt('Work\\Data\\data.txt', delimiter=',').astype('int32')
print(output)
print(np.where(output > 50))
# print(np.where(output > 50, 1, 0))