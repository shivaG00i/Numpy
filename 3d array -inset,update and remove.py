import numpy as np

arr=np.array([[[1,2,3],[4,5,6],[8,9,0]]])
print(arr)

#insert using append
app0=np.append(arr,[1,22,88])
app00=np.append(arr,0)
print(app0)
print(app00)
print()

''' 
np.append flattens the input array (unless you specify an axis).

So it flattens arr into a 1D array:
[1, 2, 3, 4, 5, 6, 8, 9, 0]

Then appends [1, 22, 88] to that.

→ app0 = [1, 2, 3, 4, 5, 6, 8, 9, 0, 1, 22, 88]

'''

new_column = np.array([[[90], [91], [92]]])  # shape: (1, 3, 1)
app = np.append(arr, new_column, axis=2)
print(app)
print()

# [[[ 1  2  3 90]
#   [ 4  5  6 91]
#   [ 8  9  0 92]]]


new_row=np.array([[[12,34,56]]]) # shape: (1, 1, 3)
print(new_row.shape)
appen=np.append(arr,new_row,axis=1)
print(appen)

# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 8  9  0]
#   [12 34 56]]]

#insert using insert

arrinr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Original array:\n", arrinr) 
print("Shape:", arrinr.shape) # Shape: (2, 2, 2)
print()

addvalue=np.array([[[90]]])
print()
newvalue=np.insert(arrinr,0,addvalue) 
# By default, np.insert() without an axis argument will flatten the array, insert the value at the specified position, 
# and return a 1D array.
print(newvalue)
# [90  1  2  3  4  5  6  7  8]

print()
addvalue00=np.array([[[9,8],[7,4]]])
newvalue00=np.insert(arrinr,1,addvalue00,axis=0)
print(newvalue00)

''' 
You're inserting along axis=0 (blocks).
At index 1 → meaning it will be inserted between the two existing blocks.

[[[1 2]
  [3 4]]

 [[9 8]
  [7 4]]

 [[5 6]
  [7 8]]]
'''

print()
addvalue000=np.array([[[9,8]]])
newvalue000=np.insert(arrinr,2,addvalue000,axis=0)
print(newvalue000)
# NumPy will raise a ValueError, because the inserted value cannot be broadcast into the expected shape.
# axis=0

print()
addvalue1=np.array([[[9,8],[7,4]],[[4,5],[5,8]]])
newvalue1=np.insert(arrinr,0,addvalue1,axis=1)
print(newvalue1)
''' 
[[[9 8]
  [7 4]
  [1 2]
  [3 4]]

 [[4 5]
  [5 8]
  [5 6]
  [7 8]]]


'''
print()
addvalue12=np.array([[[9,8],[7,4]],[[4,5],[5,8]]])
newvalue12=np.insert(arrinr,0,addvalue12,axis=2)
print(newvalue12)

''' 
[[[9 8 1 2]
  [7 4 3 4]]

 [[4 5 5 6]
  [5 8 7 8]]]

'''
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
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

print()
print(update3DArr[1])
# [[91 92 93]
#  [94 95 96]
#  [97 98 99]]



#update value at 0,0,2
up=update3DArr[0,1,2]=888
# pdate3DArr[0, 1, 2] refers to:
# Block 0 (first block)
# Row 1 (second row)
# Column 2 (third column)
print(up)
print(update3DArr)
print()
# 888
# [[[ 10  20  30]
#   [ 40  50 888]
#   [ 70  80  90]]

#  [[ 91  92  93]
#   [ 94  95  96]
#   [ 97  98  99]]]


# update value at whole 0,2 row
update3DArr[0,2]=[91,92,93]
print(update3DArr)
print()
# [[[ 10  20  30]
#   [ 40  50 888]
#   [ 91  92  93]] --> [70, 80, 90]

#  [[ 91  92  93]
#   [ 94  95  96]
#   [ 97  98  99]]]

# update value at whole 1,:,2 coloumn
update3DArr[1,:,2]=[1,2,3]
print(update3DArr)
print()
''' 
update3DArr[1, :, 2] means:

Block 1 (the second 2D array),
All rows (:),
Column 2 (the third column).
You’re replacing the entire third column of block 1 with [1, 2, 3].

[[[ 10  20  30]
  [ 40  50 888]
  [ 91  92  93]]

 [[ 91  92   1]
  [ 94  95   2]
  [ 97  98   3]]]


'''
# update value at  1,0,1
update3DArr[1,0,1]=77
print(update3DArr)
print()
''' 
update3DArr[1, 0, 1] means:
Block 1 (second block)
Row 0 (first row)
Column 1 (second column)

Originally, that element was 92. You replaced it with 77.
[[[ 10  20  30]
  [ 40  50 888]
  [ 91  92  93]]

 [[ 91  77   1]
  [ 94  95   2]
  [ 97  98   3]]]


'''
# update a[1]

update3DArr[1]=[
    [1,3,4],
    [9,8,0],
    [5,2,1]
]
print(update3DArr)

''' 

[[[ 10  20  30]
  [ 40  50 888]
  [ 91  92  93]]

 [[  1   3   4]
  [  9   8   0]
  [  5   2   1]]]

'''
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
''' 
After deleting slice 0:
 [[[21 22 23]
   [24 25 26]
   [27 28 29]]]

'''
#🔹 2. Delete a row from each slice – axis=1

delarr2 = np.delete(delarr, 1, axis=1)  # delete row index 1 from each slice
print("After deleting row 1 in each slice:\n", delarr2)

''' 
After deleting row 1 in each slice:
 [[[11 12 13]
   [17 18 19]]

  [[21 22 23]
   [27 28 29]]]

'''

#🔹 3. Delete a column from each row in each slice – axis=2
delarr3 = np.delete(delarr, 2, axis=2)  # delete column index 2
print("After deleting column 2 in each row:\n", delarr3)
''' 
After deleting column 2 in each row:
 [[[11 12]
   [14 15]
   [17 18]]

  [[21 22]
   [24 25]
   [27 28]]]

'''

#🔹 4. Delete a specific element? (⚠️ Not allowed in NumPy)

del delarr
# print(delarr)

# Optional: Clear contents instead of deleting
# arr = np.empty((0, 0, 0))  # sets it to an empty 3D array




