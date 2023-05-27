import pandas as pd

nums = ["one", "two", "three", "four", "five"]
nums_series = pd.Series(nums, [chr(x + 65) for x in range(len(nums))])

country_list = "United States, France, Germany, Italy"
countries = pd.Series(country_list.split(" "))
