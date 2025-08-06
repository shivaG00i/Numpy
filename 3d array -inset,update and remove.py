import numpy as np

arr=np.array([[[1,2,3],[4,5,6],[8,9,0]]])
print(arr)

#insert using append
app0=np.append(arr,[1,22,88])
app00=np.append(arr,0)
print(app0)
print(app00)
print()

new_column = np.array([[[90], [91], [92]]])  # shape: (1, 3, 1)
app = np.append(arr, new_column, axis=2)
print(app)
print()

new_row=np.array([[[12,34,56]]]) # shape: (1, 1, 3)
print(new_row.shape)
appen=np.append(arr,new_row,axis=1)
print(appen)

#insert using insert

arrinr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Original array:\n", arrinr)
print("Shape:", arrinr.shape)
print()

addvalue=np.array([[[90]]])
print()
newvalue=np.insert(arrinr,0,addvalue)
print(newvalue)

print()
addvalue00=np.array([[[9,8],[7,4]]])
newvalue00=np.insert(arrinr,1,addvalue00,axis=0)
print(newvalue00)

print()
addvalue000=np.array([[[9,8]]])
newvalue000=np.insert(arrinr,2,addvalue000,axis=0)
print(newvalue000)

print()
addvalue1=np.array([[[9,8],[7,4]],[[4,5],[5,8]]])
newvalue1=np.insert(arrinr,0,addvalue1,axis=1)
print(newvalue1)

print()
addvalue12=np.array([[[9,8],[7,4]],[[4,5],[5,8]]])
newvalue12=np.insert(arrinr,0,addvalue12,axis=2)
print(newvalue12)


# update an 3D array



update3DArr = np.array([
    [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]],

    [[91, 92, 93],
     [94, 95, 96],
     [97, 98, 99]]
])

print("Original array:\n", update3DArr)
print("Shape:", update3DArr.shape)  # (2, 3, 3)

print(update3DArr[0])
print()
print(update3DArr[1])


#update value at 0,0,2
up=update3DArr[0,1,2]=888
print(up)
print(update3DArr)
print()

# update value at whole 0,2 row
update3DArr[0,2]=[91,92,93]
print(update3DArr)
print()

# update value at whole 1,:,2 coloumn
update3DArr[1,:,2]=[1,2,3]
print(update3DArr)
print()

# update value at  1,0,1
update3DArr[1,0,1]=77
print(update3DArr)
print()

# update a[1]

update3DArr[1]=[
    [1,3,4],
    [9,8,0],
    [5,2,1]
]
print(update3DArr)


# delete an 3D array



delarr = np.array([
    [[11, 12, 13],
     [14, 15, 16],
     [17, 18, 19]],

    [[21, 22, 23],
     [24, 25, 26],
     [27, 28, 29]]
])

print("Original array:\n", delarr)
print("Shape:", delarr.shape)  # (2, 3, 3)

# 🔹 1. Delete a slice (entire 2D matrix) – axis=0

delarr1 = np.delete(delarr, 0, axis=0)  # delete slice at index 0
print("After deleting slice 0:\n", delarr1)

#🔹 2. Delete a row from each slice – axis=1

delarr2 = np.delete(delarr, 1, axis=1)  # delete row index 1 from each slice
print("After deleting row 1 in each slice:\n", delarr2)

#🔹 3. Delete a column from each row in each slice – axis=2
delarr3 = np.delete(delarr, 2, axis=2)  # delete column index 2
print("After deleting column 2 in each row:\n", delarr3)

#🔹 4. Delete a specific element? (⚠️ Not allowed in NumPy)

del delarr
# print(delarr)

# Optional: Clear contents instead of deleting
# arr = np.empty((0, 0, 0))  # sets it to an empty 3D array



