import numpy as np


# arr1 = np.array([x for x in range(10)])

# print("np.array {0:>20} ".format(arr1))
# print("np.array {0:>20} ".format(arr1.ndim))
# print("np.array {0:>20} ".format(arr1.shape))
# print("np.array {0:>20} ".format(arr1.size))
# print("np.array {0:>20} ".format(arr1.dtype))
# print("np.array {0:>20} ".format(str(arr1d)))

rng = np.random.default_rng(31)
rand_int = rng.integers(1, 10, 5, endpoint=True)
print("random 5 integers : ", rand_int, "\n")

r_float = rng.random(10)
print(r_float)
print("-" * 50)
# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# Flip the array along the first axis (rows)
flipped_arr_axis0 = np.flip(arr, axis=0)
print(arr, " ", flipped_arr_axis0)

# Flip the array along the second axis (columns)
flipped_arr_axis1 = np.flip(arr, axis=1)

print("-" * 50)
print(flipped_arr_axis1)
