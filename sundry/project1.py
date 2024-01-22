import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import warnings

pd.set_option("display.max_columns", 100)
warnings.filterwarnings("ignore")
# %run PandasDataframeFunctions.ipynb
# pdf=PandasDataframeFunctions
# %run 'jupyter_display.ipynb'
imdb_movie = pd.read_csv(
    "https://github.com/akladyous/imdb_movie_analysis/raw/main/data/IMDb%20movies.csv",
    low_memory=False,
)
imdb_ratings = pd.read_csv(
    "https://github.com/akladyous/imdb_movie_analysis/raw/main/data/IMDb%20ratings.csv"
)


imdb = pd.merge(
    imdb_movie, imdb_ratings, left_on="imdb_title_id", right_on="imdb_title_id"
)
# pdf.dropcol(imdb,60)
imdb.drop(imdb[imdb["year"].str.contains("[A-Za-z]")].index, inplace=True)
imdb["year"] = imdb["year"].astype(np.dtype("int32"))
if imdb["votes"].equals(imdb["total_votes"]):
    imdb.drop("votes", axis=1, inplace=True)
imdb.drop_duplicates(subset=["title"], keep="last", inplace=True)
imdb.dropna(subset=["country"], inplace=True)
