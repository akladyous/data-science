import pandas as pd


movies = pd.read_csv("http://bit.ly/imdbratings")

# --------------------------------------------------------------------
# l1 = []
# for length in movies.duration:
#     if length >= 200:
#         l1.append(True)
#     else:
#         l1.append(False)

# is_long = pd.Series(l1)
# print(is_long.head(5))
# --------------------------------------------------------------------
l1 = [length for length in movies.duration >= 200]
is_long = pd.Series(l1)
print(is_long.head(5))
# --------------------------------------------------------------------
print(movies[is_long])

print(movies.duration >= 200)  # Boolean Result

print(movies[movies.duration >= 200])
