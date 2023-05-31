import pandas as pd
import numpy as np

countries_db = pd.read_csv("./data/countries_with_code.csv.gz", index_col="code")
countries = countries_db["name"]
# print("countries : ", countries)

# italia_egitto = countries_db.loc["IT":"EG"]
print(countries_db.loc["EG":"IT"])
