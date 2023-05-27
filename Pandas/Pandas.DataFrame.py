from pandas import DataFrame as df
import numpy as np

df1 = df(np.arange(16).reshape(4, 4), index=('row' + str(x)
                                             for x in range(4)), columns=('column' + str(x) for x in range(4)))

print(df1)

# print(df1.loc['row1'])
