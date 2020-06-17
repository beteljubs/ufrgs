import matplotlib.pyplot as plt
import numpy as np

def f1(x, v):  # dx/dt = v
    f = v
    return f

def f2(v, x):  # dv/dt = - k/m * x
    f = - w02 * x
    return f

w02 = 3
tmax = 50
h = .01
t0 = 0
x0 = 2
v0 = 1

t = []
x = []
v = []

t_n = t0
x_n = x0
v_n = v0

while (t_n <= tmax):
    vnovo = v_n + f2(v_n, x_n) * h
    xnovo = x_n + f1(x_n, vnovo) * h
    t.append(t_n)
    v.append(v_n)
    x.append(x_n)
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

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.scatter(x, v, s=.5)
plt.savefig(arquivo2)
plt.show()
