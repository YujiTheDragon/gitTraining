import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import psutil

x = [1]
y = [psutil.cpu_percent(1)]

fig, ax = plt.subplots()
graph = ax.plot(x, y, color="g")[0]
plt.ylim(0, 100)


def DisplayData():

    anim = FuncAnimation(fig, updateFrame, frames=None)
    plt.show()


def updateFrame(frame):
    global graph

    x.append(x[-1] + 1)
    y.append(psutil.cpu_percent(1))

    graph.set_xdata(x)
    graph.set_ydata(y)
    plt.xlim(x[0], x[-1])
