import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from scipy import stats

np.random.seed(5)
X = np.arange(20, 60) # AGEs 
# Y = np.linspace(25000,40000,40).astype(int) # INCOMEs
# Y = np.random.normal(loc=30000, scale=.5, size=40)# INCOMEs
Y = np.sort(np.random.randint(25000, 35000, size=40))# INCOMEs

#df = pd.DataFrame({'year': year, 'income':income})


#y = b0 + b1x + e

slope, intercept, r, p, se=stats.linregress(X,Y)


#calculate correlation coefficient

# def pearson(x,y):
#     nominator = 0
#     denominator = 0    
#     for i in range(len(x)):
#         nominator   += ( X[i] - np.mean(X)) * (Y[i] - np.mean(Y))

#         denominator += ((X[i] - np.mean(X))**2)  * ((Y[i]-np.mean(Y))**2)
#     return nominator / np.sqrt(denominator)
# pearson(X,Y)