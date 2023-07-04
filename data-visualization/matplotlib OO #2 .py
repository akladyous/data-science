import matplotlib.pyplot as plt
import numpy as np

def create_plot():
    xs=[]
    ys=[]
    for x in range(1,11):
        xs.append(x)
        # ys.append(np.linspace(0,1,10))
        ys.append(np.random.randint(20))
    return xs, ys

fig = plt.figure()

x, y = create_plot()
ax1 = fig.add_subplot(2,2,1)
ax1.set_title("ax 1")
ax1.set_xlabel("X label")
ax1.set_ylabel("Y label")
# ax1.set_xlim(xmin=x[0], xmax=x[-1])

ax1.plot(x,y, linestyle='-', color="k", label='ax1 legend')
ax1.legend(loc='upper left')

# ------------------------------------------------------------
ax2 = fig.add_subplot(242, label='ax2')
ax2.set_title("ax 2")
ax3 = fig.add_subplot(223, label='ax3')
ax3.set_title("ax 3")

ax4=fig.add_axes([.7,.3,.2,.6])
ax4.set_title("ax 4")


plt.show()