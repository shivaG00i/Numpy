import numpy as np

arr=np.array([1,8,5,8])

arr2=np.array([[6,9,7],[6,4,1]])


# find len
l=len(arr)
ll=len(arr2)
print(l)
print(ll)
print()
# find no elements
s=np.size(arr)
ss=np.size(arr2)
print(s)
print(ss)
# find diamention

dim1=np.ndim(arr)
dim2=np.ndim(arr2)

print(dim1,dim2)
#find te type
print(arr.dtype)
print(arr2.dtype)

#convert to type
print(arr.astype(np.int16))
print(arr2.astype(np.int16))

# find the shape
shape1=np.shape(arr)
shape2=np.shape(arr2)

print(shape1)
print(shape2)


# float array

a=[2.4,7.8,9.0,0.8]

a1=np.array([a])
print(a1)


print(a1.astype(int))