#!/usr/bin/python

###########################################
# module: graph_drv.py
#Krista Gurney
#A01671888
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt
import math

def graph_drv(fexpr, xlim, ylim):
    f1 = tof(fexpr)
    f2 = tof(deriv(fexpr))

    xvals = np.linspace(-2, 2, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim()
    plt.xlim()
    plt.grid()
    plt.plot(xvals, yvals1, label=fexpr.__str__(), c='r')
    plt.plot(xvals, yvals2, label=deriv(fexpr).__str__(), c='g')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    prd = prod(mult1=make_const(2.0), mult2=make_pwr('x', 5.0))
    graph_drv(prd, [-3.0, 3.0], [-50.0, 50.0])
