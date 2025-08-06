
import numpy as np

# 1D array slicing
arra1d=np.array([3,5,7,9])

print(arra1d[0])
print(arra1d[-1])
print(arra1d[0:3])
print(arra1d[0:4])
# print(arra1d[0:5])

# 2D array slicing
arra2d=np.array([[1,6,8,4],[5,7,6,9],[7,3,1,3]])

print(arra2d[0])
print(arra2d[-1])
print()
print(arra2d[0:3])
print()
print(arra2d[0:4])
print(arra2d[0,0:2])
print(arra2d[0,0:3])
print()
print(arra2d[1,0:2])
print(arra2d[2,0:2])


# 3D array slicing
arra3d=np.array([[[1,2,3],[5,9,7],[9,3,1]]])
print(arra3d)
print()

print(arra3d[0]) # layer
print(arra3d[0,0]) # row
print(arra3d[0,0,0]) # value at index

print()

print(arra3d[0,1])
print(arra3d[0,1,0])
print(arra3d[0,1,2])
# print(arra3d[0,1,3])

print()

print(arra3d[0,0,0:2])
print(arra3d[0,1,0:3])
print(arra3d[0,2,-3:-1])
