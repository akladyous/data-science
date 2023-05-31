import pandas as pd
import numpy as np

nums = ["one", "two", "three", "four", "five"]
nums_series = pd.Series(nums, [chr(x + 65) for x in range(len(nums))])

rng = np.random.default_rng(123)
random_integers = rng.integers(1, 10, 10)
random_decimals = rng.random(10)
normal_distribution = rng.normal(2, 1, 10)

s1 = pd.Series(
    random_integers,
    index=[f"n_{x}" for x in random_integers],
    dtype=np.int8,
    name="Random Integers",
)
print(s1)
print("-" * 50)

s2_data = {chr(97 + x): x for x in range(5)}
s2_indexes = list(map(lambda x: x.upper(), s2_data.keys()))
s2 = pd.Series(
    data=s2_data,
    dtype=np.int8,
    name="Dict Comprehension",
)
print(s2)
print(s2.iloc[0:2])
print(s2.loc["c"])
print("-" * 50)
