# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 21:28:05 2014

@author: swoop
"""

import matplotlib.pyplot as plt

plt.plot([-10,8],[-4,5]) #paired [x] and [y] cooridnates

plt.title('this is the damned title')
plt.xlabel('this is the x')
plt.ylabel('this is the y')

(8,-4)

import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,7,3,5])
pylab.title('hey, it works')
pylab.show()