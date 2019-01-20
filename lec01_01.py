#!/usr/bin/python

# source code to generate the graph on slide 16
# of lecture 1.
# bugs to vladimir kulyukin on canvas.

import numpy as np
import matplotlib.pyplot as plt

def lec_01_01():
    def f1(x): return x**2
    def f2(x): return 2*x - 1
    xvals = np.linspace(-2, 2, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Slope of a Curve at a Point')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([0, 5])
    plt.xlim([-2, 2])
    plt.grid()
    plt.plot(xvals, yvals1, label='y=x^2', c='r')
    plt.plot(xvals, yvals2, label='y=2x-1', c='g')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    lec_01_01()