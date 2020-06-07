# resolução da EDO dx/dt = x para x(0) = 1
# solução exata: t = exp(x)

import matplotlib.pyplot as plt
import numpy as np

# função para o método de euler
def f(u):
    return u

# resultado exato da função
def ext(t):
    u = np.exp(t)
    return u

# problema de valor inicial
# dx/dt = x; x(t = 0) = 1
t_n = 0
u_n = 1
u_n_ext = 1

# listas de valores dos eixos
t = []
u = []
u_ext = []

# valor do passo
h = .01

for i in range (0, 2000):
    # adicionando valores aos vetores
    t.append(t_n)
    u.append(f(u_n))
    u_ext.append(ext(t_n))

    # acrescentando aos valores
    t_n += h
    u_n += h * f(u_n)

# plot dos gráficos
plt.plot(t, u)
plt.plot(t, u_ext)
plt.show()

# print dos valores em um arquivo
arq = open('valores.dat', 'w')

i = 0

for i in range (0, 2000):
    str_u = str(u[i])
    str_u_ext = str(u_ext[i])
    arq.write(str_u + " ")
    arq.write(str_u_ext + "\n")

arq.close()
