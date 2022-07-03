import numpy as np
import matplotlib.pyplot as plt

randvar = np.loadtxt("Y.dat","double")

plt.grid()
plt.scatter(randvar)
plt.show()