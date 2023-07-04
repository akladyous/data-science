from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("./data.csv")
ages = data["Age"]
ages_bins = list(range(10, 100, 10))
median_ages = 29  # np.mean(ages) !!

plt.style.use("fivethirtyeight")
plt.hist(ages, bins=ages_bins, color="green", edgecolor="black", log=True, label="Ages")
plt.axvline(median_ages, color="red", label="Age Median", linewidth=2)
plt.title("Ages Survey")
plt.xlabel("Agesl")
plt.ylabel("Top Respondents")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()