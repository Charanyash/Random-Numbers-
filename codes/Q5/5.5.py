import numpy as np
import math
Y = np.loadtxt("Y.dat","double")
X = np.loadtxt("bern.dat","double")

count_0 = 0
count_1 = 0

for i in range(len(Y)):
    if X[i] - 1 == 1e-9 and Y[i] < 1e-9:
        count_0 += 1
    elif X[i] + 1 == 1e-9 and Y[i] > 1e-9:
        count_1 += 1
Prob_0  = count_0/(len(Y)/2.0)

Prob_1 = count_1*2/len(Y)

def Q(x):
	return (math.erfc(x/math.sqrt(2)))/2.0
def cdf(x):
	return Q(-x)

A = 5
print(cdf(-A))

print(Prob_0)                
print(Prob_1)