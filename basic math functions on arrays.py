import numpy as np


arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([3, 7, 9, 6])

# addition
a1=arr1+arr2
print(np.add(arr1,arr2))
print(a1)
print()
#substract
a2=arr1-arr2
print(np.subtract(arr1,arr2))
print(a2)
print()
# multiply
a3=arr1*arr2
print(np.multiply(arr1,arr2))
print(a3)
print()
#divide
a4=arr1/arr2
print(np.divide(arr1,arr2))
print(a4)
#modulo
a5=arr1%arr2
print(np.mod(arr1,arr2))
print(a5)



print()

#exp
print(np.exp(arr1))
print(np.exp(arr2))
print()
#sqrt
print(np.sqrt(arr1))
print(np.sqrt(arr2))

#sum
print(np.sum(arr1))
print(np.sum(arr2))
print()
print(sum(arr1))
print(sum(arr2))
#max and min
print()
print(max(arr1))
print(max(arr2))
print(min(arr1))
print(min(arr2))
print()

print(np.max(arr1))
print(np.max(arr2))
print(np.min(arr1))
print(np.min(arr2))