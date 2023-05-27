import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style


def create_plot():
    xs=[]
    ys=[]
    for x in range(1,11):
        xs.append(x)
        ys.append(np.random.randint(40))
    return xs, ys
        

# x = np.linspace(1,10,100)

#   style.use('fivethirtyeight')
fig = plt.figure(figsize=(6,6))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

# ------------------------------
x,y = create_plot()
ax1.plot(x,y)
ax1.set_ylabel=('y ax1')
ax1.set_xlabel=('x ax1')
# ------------------------------
x,y = create_plot()
ax2.plot(x,y)
# ------------------------------
x,y = create_plot()
ax3.plot(x,y)
# ------------------------------
plt.show()

