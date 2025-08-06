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

# creating ones Array
arr1=np.ones((2,2))
print(arr1)

print()
#creating full Array
full=np.full((2,3),5)
print(full)

print()

#creating arange Array
arna=np.arange(0,21,2)
print(arna)

print()

#creating linspace Array

line=np.linspace(0,10,5)
print(line)

print()

#creating random Array
rand1=np.random.rand(2,2)
print(rand1)

print()

rand2=np.random.randint(1,9,(2,3))
print(rand2)

#creating eye/identity Array/matrix

eye=np.eye(7)
print(eye)
