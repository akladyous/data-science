from matplotlib import pyplot as plt
import numpy as np


def create_xy():
    xs=[]
    ys=[]
    for x in range(10):
        xs.append(x)
        ys.append(np.random.randint(90))
    return xs, ys

plt.xlabel('y label')
plt.ylabel('y label')
plt.title('title x y')

x1, y1 = create_xy()
plt.plot(x1,y1, label="legend x1 y1", color='k')


x2,y2 = create_xy()
plt.plot(x1, x2, label='legend x1 x2', color='b')
plt.grid(True)
plt.legend()
plt.show()

