import numpy as np
import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fib_spy(turn, n):
    points=[]
    for i in np.arange(n):
        dst = i/(n-1.0)
        angle = np.pi * turn * i
        points.append([dst*np.cos(angle), dst*np.sin(angle)])
    
    x, y = zip(*points)
    return x, y

def update(turn, num):
    x, y = fib_spy(turn, num)
    ax.clear()
    ax.axis([-1,1,-1,1])
    ax.plot(x, y, '.')
    fig.canvas.draw_idle()

def fib(num):
    seq = []
    a = 0
    b = 1
    while a + b < num:
        seq.append(a + b)
        c = a + b
        a = b
        b = c

    return seq

num=1000
colors = np.ones(num)


fig, ax = plt.subplots()
x, y = fib_spy(2**(1/2), num)
ax.scatter( x, y, s=4, c=colors, cmap='viridis')
ax.axis('equal')


plt.show()