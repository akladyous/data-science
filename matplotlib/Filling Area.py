
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

mean_salaries = np.round(np.mean(dev_salaries), 2)
print(mean_salaries)

plt.title('Avarage Develeper Salary in USA')
plt.tight_layout()
plt.plot(ages, dev_salaries, label='Developer', color='red', linestyle='-')
plt.plot(ages, py_salaries, label='python', color='green', linestyle='-')


plt.fill_between(ages, py_salaries, mean_salaries,
                 where=(py_salaries > mean_salaries) ,interpolate=True, color='gray', alpha=0.25, label='Above Average')

plt.fill_between(ages, py_salaries, mean_salaries,
                 where=(py_salaries < mean_salaries), interpolate=True, color='cyan', alpha=0.25, label='Below Average')

plt.fill_between(ages, py_salaries, dev_salaries,
                 interpolate=True, color='yellow', alpha=0.25, label='Python ~ Dev.')
plt.legend(loc='upper left')
plt.show()
