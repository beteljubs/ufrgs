'''
EXERCICIO DE PROBLEMA INICIAL
u'(t) = 2u(t)
u(0) = 1
'''

import matplotlib.pyplot as plt
import numpy as np

def f(t, u):
    u = 2*u
    return u

def ext(t):
    u = np.exp(2*t)
    return u

u_n = 1
t_n = 0

u = []
t = []
u_ext = []

h = 0.001

for i in range (0, 2000):
    t.append(t_n)
    u.append(u_n)
    u_ext.append(ext(t_n))
    u_n += f(t_n, u_n) * h
    t_n += h

lbl1 = "método de Euler"
lbl2 = "solução analítica"

plt.plot(t, u_ext, label= lbl2)
plt.plot(t, u, label= lbl1)
plt.legend()
plt.show()
