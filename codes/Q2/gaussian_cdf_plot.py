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
	return (math.erfc(x/math.sqrt(2)))/2.0
def cdf(x):
	return Q(-x)

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list


randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

gauss_cdf = scipy.vectorize(cdf)
	
plt.plot(x.T,err,"o")#plotting the CDF
plt.plot(x,gauss_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theoritical"])

plt.savefig('figs/gauss_cdf.png')

plt.show() #opening the plot window