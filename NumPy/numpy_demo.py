import numpy as np


# arr1 = np.array([x for x in range(10)])

# print("np.array {0:>20} ".format(arr1))
# print("np.array {0:>20} ".format(arr1.ndim))
# print("np.array {0:>20} ".format(arr1.shape))
# print("np.array {0:>20} ".format(arr1.size))
# print("np.array {0:>20} ".format(arr1.dtype))
# print("np.array {0:>20} ".format(str(arr1d)))

rng = np.random.default_rng(5)
x = rng.integers(1, 10, 5)
print(np.sum(x))

r1 = rng.random(10)
print(r1)

import math

math.sin()
