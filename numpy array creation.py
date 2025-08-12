import numpy as np

# creating 1D Array

arr1d=np.array([1,2,3])
# print(arr1d)

print()

# creating 2D Array
arr2d=np.array([[1,2,3],[4,5,6]])
# print(arr2d)

print()

# creating 3D Array
arr3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr3d)

# creating zero Array

arr0=np.zeros((2,3)) #shape
print(arr0)
print()

# [[0. 0. 0.]
#  [0. 0. 0.]]


# creating ones Array
arr1=np.ones((2,2))
print(arr1)
print()

# [[1. 1.]
#  [1. 1.]]

#creating full Array
full=np.full((2,3),5)
print(full)
print()

# [[5 5 5]
#  [5 5 5]]


#creating arange Array
arna=np.arange(0,21,2) # So: start = 0, stop = 21, step = 2
print(arna)

#[ 0  2  4  6  8 10 12 14 16 18 20]

print()

#creating linspace Array

line=np.linspace(0,10,5) #start = 0 stop = 10 num = 5
print(line)

# [ 0.   2.5  5.   7.5 10. ]
print()       
                                                  # Use rand() for floating-point numbers in [0, 1).

                                                  # Use randint() for integers in a specified range.

#creating random Array
rand1=np.random.rand(2,2)
print(rand1)

print()

# [[0.37454012 0.95071431]
#  [0.73199394 0.59865848]]


rand2=np.random.randint(1,9,(2,3))
print(rand2)

# np.random.randint(1, 9, (2, 3)) means:
# Generate random integers from 1 to 8 (upper bound is exclusive).
# Shape: 2 rows, 3 columns → shape (2, 3)

# [[7 5 3]
#  [1 8 4]]


#creating eye/identity Array/matrix

eye=np.eye(7)
print(eye)

# np.eye(7) creates a 7×7 identity matrix.
# All diagonal elements = 1, others = 0.

# [[1. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1.]]



