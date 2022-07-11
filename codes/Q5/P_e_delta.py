import matplotlib.pyplot as plt
import scipy
import math
import numpy as np

def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2.0

def error(delta,a):
    x = np.loadtxt("bern.dat",dtype = "double")
    n = np.loadtxt("gau.dat",dtype = "double")
    y = a*x + n
    x_0 = np.count_nonzero(x>0)
    x_1 = np.count_nonzero(x<0)
    y_0 = np.count_nonzero((y<delta)&(x>0))
    y_1 = np.count_nonzero((y>delta)&(x<0))
    error_0  = y_0/x_0
    error_1 = y_1/x_1

    return (error_0 + error_1)/2

vec_error = scipy.vectorize(error)

vec_q = scipy.vectorize(Q)

delta = np.linspace(-10,10,30)

A = 5 

plt.plot(delta,(vec_q(A - delta) + vec_q(delta + A))/2.0)#Theoritical

plt.plot(delta,vec_error(delta,A),"o") # Numerical
plt.grid()

plt.legend(["Theoritical","Numerical"])

plt.savefig("P_e_delta.png")

plt.show()