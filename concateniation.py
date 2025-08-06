# # Excellent! Let's walk through **concatenation and stacking methods in NumPy** — how they work across **1D, 2D, and 3D arrays**, with examples and outputs.
# #
# # ---
# #
# # ## ✅ Main Methods for Combining Arrays
# #
# # | Method           | Purpose                             | Axis Control | Flattens? |
# # | ---------------- | ----------------------------------- | ------------ | --------- |
# # | `np.concatenate` | Joins arrays along an existing axis | ✅ Yes        | ❌ No      |
# # | `np.stack`       | Joins arrays along a new axis       | ✅ Yes        | ❌ No      |
# # | `np.hstack`      | Horizontal stack (columns)          | ❌ Axis=1     | ❌ No      |
# # | `np.vstack`      | Vertical stack (rows)               | ❌ Axis=0     | ❌ No      |
# #
# # ---
#
# import numpy as np
# ## 🔹 1D Arrays Example
#
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
#
# ### 🔸 `np.concatenate`
#
# np.concatenate((a, b))  # ➡️ [1 2 3 4 5 6]
#
#
# ### 🔸 `np.stack`
#
# ```python
# np.stack((a, b))        # ➡️ shape (2, 3)
# # Output:
# # [[1 2 3]
# #  [4 5 6]]
# ```
#
# ### 🔸 `np.hstack`
#
# ```python
# np.hstack((a, b))       # ➡️ [1 2 3 4 5 6]
# ```
#
# ### 🔸 `np.vstack`
#
# ```python
# np.vstack((a, b))       # ➡️ shape (2, 3)
# # [[1 2 3]
# #  [4 5 6]]
# ```
#
# ---
#
# ## 🔹 2D Arrays Example
#
# ```python
# a2 = np.array([[1, 2], [3, 4]])
# b2 = np.array([[5, 6], [7, 8]])
# ```
#
# ### 🔸 `np.concatenate`
#
# ```python
# np.concatenate((a2, b2), axis=0)  # ➡️ shape (4, 2)
# # [[1 2]
# #  [3 4]
# #  [5 6]
# #  [7 8]]
# ```
#
# ```python
# np.concatenate((a2, b2), axis=1)  # ➡️ shape (2, 4)
# # [[1 2 5 6]
# #  [3 4 7 8]]
# ```
#
# ### 🔸 `np.stack`
#
# ```python
# np.stack((a2, b2), axis=0)  # ➡️ shape (2, 2, 2)
# ```
#
# ### 🔸 `np.hstack`
#
# ```python
# np.hstack((a2, b2))  # ➡️ shape (2, 4)
# # [[1 2 5 6]
# #  [3 4 7 8]]
# ```
#
# ### 🔸 `np.vstack`
#
# ```python
# np.vstack((a2, b2))  # ➡️ shape (4, 2)
# # [[1 2]
# #  [3 4]
# #  [5 6]
# #  [7 8]]
# ```
#
# ---
#
# ## 🔹 3D Arrays Example
#
# ```python
# a3 = np.array([
#     [[1, 2], [3, 4]]
# ])
# b3 = np.array([
#     [[5, 6], [7, 8]]
# ])
# ```
#
# ### Shape: `(1, 2, 2)`
#
# ### 🔸 `np.concatenate`
#
# ```python
# np.concatenate((a3, b3), axis=0)  # ➡️ shape (2, 2, 2)
# ```
#
# ### 🔸 `np.stack`
#
# ```python
# np.stack((a3, b3), axis=0)  # ➡️ shape (2, 1, 2, 2)
# ```
#
# ### 🔸 `np.hstack`
#
# ```python
# np.hstack((a3, b3))  # ➡️ shape (1, 2, 4)
# # [[ [1 2 5 6]
# #     [3 4 7 8] ]]
# ```
#
# ### 🔸 `np.vstack`
#
# ```python
# np.vstack((a3, b3))  # ➡️ shape (2, 2, 2)
# ```
#
# ---
#
# ## 🧠 Summary Table
#
# | Operation     | New Axis | Combines Along   | Works On | Notes                                       |
# | ------------- | -------- | ---------------- | -------- | ------------------------------------------- |
# | `concatenate` | ❌ No     | Existing axis    | All      | Needs matching shape except for axis joined |
# | `stack`       | ✅ Yes    | New axis         | All      | Adds dimension; shape grows                 |
# | `hstack`      | ❌ No     | Columns (axis=1) | ≥1D      | Horizontally stacks side-by-side            |
# | `vstack`      | ❌ No     | Rows (axis=0)    | ≥1D      | Vertically stacks on top                    |
#
# ---
#
# Let me know if you'd like **graphical visualization** or if you're working with **arrays of different shapes** — I can show tricks using `reshape()` or `np.newaxis` to make them compatible!
