import matplotlib.pyplot as plt
# import numpy as np

plt.style.use(("fivethirtyeight"))
plt.tight_layout()

plt.title("awsome chart")


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0, 0, 0, 0.1, 0]
plt.pie(slices, explode=explode, labels=labels,
        shadow=True, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'}, startangle=90)
plt.show()