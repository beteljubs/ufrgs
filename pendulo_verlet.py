# Pendulo pelo método de Verlet

import numpy as np
import matplotlib.pyplot as plt

def alpha(theta):
    a = k*np.sin(theta)
    return a

w0 = 0
h = 0.01
theta0 = 1.5  # theta(n)
t0 = 0

g = 10
L = 1
k = -g/L

theta_a = theta0 + w0*h + .5 * alpha(theta0) * (h**2)  # theta(n-1)

theta = []
w = []
t = []

for i in range (0,1000):
    theta.append(theta0)
    t.append(t0)
    theta1 = 2*theta0 - theta_a + alpha(theta0) * (h**2)  # theta(n+1)
    theta_a = theta0
    theta0 = theta1
    t0 += h

plt.plot(t, theta)
plt.show()
