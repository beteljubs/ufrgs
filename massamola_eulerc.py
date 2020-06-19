import matplotlib.pyplot as plt
import numpy as np

def f1(x, v):  # dx/dt = v
    f = v
    return f

def f2(v, x):  # dv/dt = - k/m * x
    f = - w02 * x
    return f

def Ec(v):
    E = (1/2) * (m * (v**2))
    return E

def Ep(x):
    E = (1/2) * (k * (x**2))
    return E

w02 = 3
tmax = 100
h = .01
t0 = 0
x0 = 2
v0 = 1
m = 1
k = 3

E0 = Ec(v0) + Ep(x0)

t = []
x = []
v = []
E = []

t_n = t0
x_n = x0
v_n = v0

while (t_n <= tmax):
    vnovo = v_n + f2(v_n, x_n) * h
    xnovo = x_n + f1(x_n, vnovo) * h
    t.append(t_n)
    v.append(v_n)
    x.append(x_n)
    Et = Ec(v_n) + Ep(x_n)
    E.append((Et - E0)/E0)
    v_n = vnovo
    x_n = xnovo
    t_n += h

titulo = "Método de Euler-Cromer"
xlabel = "tempo"
arquivo1 = "massa-mola_eulerc1.png"
arquivo2 = "massa-mola_eulerc2.png"

plt.title(titulo)
plt.xlabel(xlabel)
plt.plot(t, x, label = "posição")
plt.plot(t,v, label = "velocidade")
plt.legend()
plt.savefig(arquivo1)
plt.show()

xlabel = "posição"
ylabel = "velocidade"

plt.title(titulo)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.scatter(x, v, s=.5)
plt.savefig(arquivo2)
plt.show()

xlabel = "tempo"
ylabel = "(E(t) - E0)/E0"
titulo = "'Flutuação' da energia x t"

plt.title(titulo)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.plot(t, E, label = "Euler-Cromer")
plt.ylim((-.05,.05))
plt.xlim((0, 10))
#plt.savefig(arquivo)
plt.show()
