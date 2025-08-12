import numpy as np

arr=np.array([2,3,4,6])

# using append method
v=np.append(arr,90)
print(v)
print()

arr2=np.array([[1,4,5],[3,8,98]])
v1=np.append(arr2,90)
print(v1)
c=v1.reshape((7,1))
print(c)

#using insert method
arr=np.insert(arr,1,9)
print(arr)

arr2=np.insert(arr2,1,88)
print(arr2)

# using inset with axis

array = np.array([[1, 2], [3, 4]])

result = np.insert(array, 1, 99)  # No axis specified
print(result)

res=np.insert(array,0,(1,7),axis=0)
print(res)

print()
rescol=np.insert(array,0,(1,7),axis=1)
print(rescol)


# delete an arra and item

delt = np.array([10, 20, 30, 40])
print(delt)
new_arr = np.delete(delt, 1)  # Deletes the item at index 1
print(new_arr)
print()

delt2=np.array([[12,89,77,4],[80,87,76,79]])
new_arr2=np.delete(delt2,0,axis=0)
print(new_arr2)
print()
#np.delete(delt2, 0, axis=0) removes the first row (index 0) along axis=0 (i.e., row-wise deletion).
# [[80 87 76 79]]


new_arr3=np.delete(delt2,1,axis=1)
print(new_arr3)

# np.delete(delt2, 1, axis=1) means:
# Delete column at index 1 (i.e., the second column) across all rows.
# [[12 77  4]
#  [80 76 79]]


#update the array

update1dArray=np.array([1,4,5])

update1dArray[2]=8
print(update1dArray)

update2DArray=np.array([[1,8,9,7],[7,6,4,1]])
update2DArray[0,0]=90 # Change element at row 0, col 0 → 90
update2DArray[0,3]=990
update2DArray[1,2]=180

print(update2DArray)    

# [[ 90   8   9 990]
#  [  7   6 180   1]]
