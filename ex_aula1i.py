# Método de Euler Implícito
# decaimento radioativo

import matplotlib.pyplot as plt
import numpy as np

def f1(N):
    N = - (a * N)
    return N

# valores iniciais
N0 = float(1000)  # num de atomos inicial
a = float(9.24*(10**(-3)))  # coef. de decaimento radioativo
t0 = 0  # tempo inicial
h = .1  # passo

# listas Euler implicito
N = []
N1_log = []
t = []

int = 0

# 2. usar os mesmos parametros e integrar usando o método de Euler imp

Nnovo = N0 / (1 + a*h)

for i in range(0, 6000):
    N.append(N0)
    t.append(t0)
    if i == (75 / h):  # t0 = 75 segundos
        print(N0)
    t0 += h
    N0 = Nnovo
    Nnovo = N0 / (1 + a*h)
    Nnovo = N0 + f1(Nnovo) * h

plt.title("método de Euler implícito")
plt.plot(t, N, color="#ff6f00")
#plt.savefig("implicito.png")
plt.show()
