import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def fib_spy(turn, n, exp = 1):
    points=[]
    for i in np.arange(n):
        dst = i**exp/(n**exp-1.0)
        angle = np.pi * turn * i
        points.append([dst*np.cos(angle), dst*np.sin(angle)])
    
    x, y = zip(*points)
    return x, y

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
x, y = fib_spy(2**(1/2), 1000)
line, = ax.plot( x, y, '.')
ax.axis('equal')


axnum = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='blue')
num_slider = Slider(ax=axnum, label='Number', valmin=0, valmax=3000, valinit=1000,)

axamp = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor='green')
turn_slider = Slider(ax=axamp, label="Angle", valmin=0, valmax=int(1000 * np.pi), valinit=2**(1/2)*1000,)

axexp = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='red')
exp_slider = Slider(ax=axexp, label="Exponent", valmin=-3, valmax=3, valinit=1,)

def update(val):
    x, y = fib_spy(turn_slider.val/1000, num_slider.val, exp_slider.val)
    ax.clear()
    ax.axis([-2,2,-2,2])
    ax.plot(x, y, '.')
    fig.canvas.draw_idle()

num_slider.on_changed(update)
turn_slider.on_changed(update)
exp_slider.on_changed(update)

plt.show()