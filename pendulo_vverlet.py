# Pêndulo simples pelo método de Velocity-Verlet

import numpy as np
import matplotlib.pyplot as plt

def alpha(theta):
    a = k*np.sin(theta)
    return a

w0 = 0
h = 0.01
theta0 = 1.5
t0 = 0

g = 10
L = 1
k = -g/L

theta = []
t = []

for i in range (0,2000):
    theta.append(theta0)
    t.append(t0)
    a1 = alpha(theta0)
    theta0 = theta0 + w0*h + .5 * a1*(h**2)
    w0 = w0 + (h/2) * (a1 + alpha(theta0))
    t0 += h

plt.plot(t, theta)
plt.show()
