import matplotlib.pyplot as plt
import numpy as np

def f1(x, v):  # dx/dt = v
    f = v
    return f

def f2(v, x):  # dv/dt = - w02 * x
    f = - w02 * x
    return f

def Ec(v):
    E = (1/2) * (m * (v**2))
    return E

def Ep(x):
    E = (1/2) * (k * (x**2))
    return E

w02 = 3
tmax = 50
h = .01
t0 = 0
x0 = 2
v0 = 1
m = 1
k = 3

E0 = Ec(v0) + Ep(x0)

print(E0)

t = []
x = []
v = []
E = []

t_n = t0
x_n = x0
v_n = v0

while (t_n <= tmax):
    xnovo = x_n + f1(x_n, v_n)*h
    vnovo = v_n + f2(v_n, x_n)*h
    t_n += h
    t.append(t_n)
    v.append(v_n)
    x.append(x_n)
    Et = Ec(v_n) + Ep(x_n)
    E.append((Et - E0)/E0)
    x_n = xnovo
    v_n = vnovo

titulo = "Método de Euler Explícito"
xlabel = "tempo"
arquivo1 = "massa-mola_eulere.png"
arquivo2 = "massa-mola_eulere2"

plt.title(titulo)
plt.xlabel(xlabel)
plt.plot(t, x, label = "posição")
plt.plot(t, v, label = "velocidade")
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
titulo = "energia x t"

plt.title(titulo)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.plot(t, E, label = "Euler")
#plt.savefig(arquivo)
plt.show()
