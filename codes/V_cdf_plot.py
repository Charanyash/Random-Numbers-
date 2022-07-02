#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math

#if using termux
import subprocess
import shlex

import scipy
#end if
def Q(x):
    if x<0:
        return 1
    else :
        return math.exp(-x/2.0)


x = np.linspace(-10,10,50)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
err1 = [] #declaring another probability list.
randvar = np.loadtxt('ray.dat',dtype='double')
for i in range(len(x)):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
for i in range(len(x)):
    c = 1 - Q(x[i])
    err1.append(c)
	
plt.plot(x.T,err,"o")#plotting the CDF
plt.plot(x,err1)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theoritical"])

plt.savefig('figs/ray_cdf.png')

plt.show() #opening the plot window
