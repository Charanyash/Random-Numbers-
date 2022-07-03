#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math 

#if using termux
import subprocess
import shlex

import scipy
#end if


x = np.linspace(-10,30,70)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list


randvar = np.loadtxt('chi.dat',dtype='double')
for i in range(0,70):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
def chi_square_cdf(x):
   if x>=0: 
    return 1 - math.exp(-x/2.0)
   else :
    return 1e-5
vec_chi_square_cdf = scipy.vectorize(chi_square_cdf)

plt.plot(x.T,err,"o")#Numerical
plt.plot(x,vec_chi_square_cdf(x))# Theoritical
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(["Numerical","Theoritical"])

plt.savefig('chi_square_cdf.png')

plt.show() #opening the plot window