# MÉTODO DE EULER EXPLÍCITO
# 1. integrar a equacao do decaimento radioativo

import matplotlib.pyplot as plt
import numpy as np

def f1(N):  # dN/dt = - a * N
    N = - (a * N)
    return N

# valores iniciais
N0 = float(1000)  # num de atomos inicial
a = float(9.24*(10**(-3)))  # coef. de decaimento radioativo
t0 = 0  # tempo inicial
h = .1  # passo

# listas
N = []
N_log = []
t = []

for i in range (0, 6000):
    N.append(N0)
    t.append(t0)
    N_log.append(np.log(N0))
    if i == (75 / h):  # t0 = 75 segundos
        print(N0)
    N0 += f1(N0) * h
    t0 += h

plt.title("método de Euler explícito")
plt.plot(t, N, color="#411452")
#plt.savefig("explicito.png")
plt.show()

#plt.plot(t, N_log)
#plt.show()
