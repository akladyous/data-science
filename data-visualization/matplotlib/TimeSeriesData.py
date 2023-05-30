from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
from datetime import datetime, timedelta

data = pd.read_csv('bitcoin-may19.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)


#print(data.head())

price_date=data['Date']
price_close=data['Close']

plt.style.use('seaborn')
plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()

plt.legend()
plt.tight_layout()
plt.show()