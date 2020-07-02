'''
considere o problema de valor inicial
x' = f(t,x) = x - t² + 1
x(0) = 0.5
determine x(t) para 0 < t < 2
implemente os 3 métodos de RK2 e estude o comportamento (i)
da solução x(t), (ii) do erro global ao final do intervalo
solução analítica:
x = (t+1)² - 0.5e^t
'''
import numpy as np
import matplotlib.pyplot as plt

#MÉTODO DE HEUN

def f(t,x):
    x = x - t*t + 1
    return x

def fa(t,x):
    x = (t+1)**2 - .5* np.exp(t)
    return x

x0 = .5

t0 = 0
tmax = 2
n = 0
h = 10**(-3)

tn = t0
xn = x0
xan = x0

k1 = f(tn,xn)
k2 = f(tn + h, xn + k1*h)

t = []
x = []
xa = []

while tn <= tmax:
    t.append(tn)
    x.append(xn)
    xa.append(xan)
    xn = xn + h*(.5*k1 + .5*k2)
    xan = fa(tn, xan)
    tn += h
    k1 = f(tn,xn)
    k2 = f(tn + h, xn + k1*h)

lbl = "numerico"
lbla = "analitico"

plt.scatter(t,xa,marker='<',s=.5,label=lbla)
plt.scatter(t,x,marker='>',s=.5,label=lbl)
plt.legend()
plt.show()
