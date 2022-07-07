import numpy as np
import matplotlib.pyplot as plt

size = 1000000
Y = np.loadtxt("Y.dat","double")
X = np.linspace(0,1,size)

plt.plot(X,Y,"o",marker = "x",markersize = 3)
plt.xlabel("n$(x 10^6)$")
plt.ylabel("Y(n)")
plt.savefig("Y.png")







