import pandas as pd
from pandas import Series
import numpy as np

nums = ["one", "two", "three", "four", "five"]
nums_series = pd.Series(nums, [chr(x + 65) for x in range(len(nums))])

country_list = "United States, France, Germany, Italy"
countries = pd.Series(country_list.split(" "))

rng = np.random.default_rng(123)
random_integers = rng.integers(1, 10, 10)
random_decimals = rng.random(10)

print("random_integers : ", random_integers)
print("random_decimals : ", random_decimals)
