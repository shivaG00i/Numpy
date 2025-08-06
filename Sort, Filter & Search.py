import numpy as np


# sort
arr=np.array([9,90,67,0])
print((arr))
print()
print(np.sort(arr))


arr2d=np.array([[1,9,6,3,0],[5,8,98,1,2]])
print(np.sort(arr2d))
print()

arr3d=np.array([
    [[1,8],[9,0]],
    [[4,2],[9,8]]
])
print(arr3d.shape)
print(np.sort(arr3d))

# search

print()
print(print())


arr1d = np.array([10, 25, 30, 25, 50])

# Find where value == 25
indices = np.where(arr1d == 25)
print("Indices where value == 25:", indices)

# Get the actual values using boolean indexing
values = arr1d[arr1d == 25]
print("Matching values:", values)

print()
print()
#🔹 2D Array Example
arr2d = np.array([
    [5, 8, 12],
    [7, 8, 9]
])

# Find where value == 8
indices = np.argwhere(arr2d == 8)
print("Indices where value == 8:\n", indices)

# Get values > 7
greater_than_7 = arr2d[arr2d > 7]
print("Values > 7:", greater_than_7)

#🔹 3D Array Example
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 2], [2, 8]]
])

# Find where value == 2
indices = np.argwhere(arr3d == 2)
print("Indices where value == 2:\n", indices)

# Get values >= 4
greater_equal_4 = arr3d[arr3d >= 4]
print("Values >= 4:", greater_equal_4)

'''


Great question! Both `np.where()` and `np.argwhere()` are used to **find elements that match a condition**, but they return **different types of results**, and are often used in different scenarios.

---

## 🔍 Key Differences

| Feature         | `np.where()`                                    | `np.argwhere()`                              |
| --------------- | ----------------------------------------------- | -------------------------------------------- |
| 📦 Return type  | A tuple of arrays, one per axis                 | A single 2D array of full coordinates        |
| 🧠 Usage        | Best for **1D or slicing**                      | Best for **2D/3D positional index tracking** |
| 🎯 Index format | `(indices_along_axis0, indices_along_axis1, …)` | `[[i, j, ...], ...]` → one row per match     |
| ⚙️ Good for     | Boolean selection / filtering                   | Row-wise indexing / loop-based logic         |

---

## ✅ Visual Example: 2D Array

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 20, 60]
])

# Where value == 20
w = np.where(arr == 20)
a = np.argwhere(arr == 20)

print("np.where output:", w)
print("np.argwhere output:\n", a)
```

### 🔸 `np.where` Output:

```
(array([0, 1]), array([1, 1]))
```

This means:

* Value 20 is found at (0,1) and (1,1)

---

### 🔸 `np.argwhere` Output:

```
[[0 1]
 [1 1]]
```

This gives you:

* Explicit coordinates as rows: `[row, col]` pairs

---

## ✅ When to Use What?

| Scenario                                     | Use             |
| -------------------------------------------- | --------------- |
| Want coordinates as tuples (for slicing)     | `np.where()`    |
| Want full row-column (or 3D index) positions | `np.argwhere()` |
| Want to filter values using boolean indexing | `np.where()`    |
| Need to iterate over matching coordinates    | `np.argwhere()` |

---

'''

#filetr


Farr1d = np.array([10, 20, 30, 40])
filtered = Farr1d[Farr1d>20]
print("Filtered 1D:", filtered)

farr2d = np.array([
    [5, 15, 25],
    [35, 10, 45]
])
filtered1 = farr2d[farr2d > 20]
print("Filtered 2D:", filtered1)

farr3d = np.array([
    [[1, 10], [20, 5]],
    [[30, 2], [3, 40]]
])
filtered2 = farr3d[farr3d > 10]
print("Filtered 3D:", filtered2)



