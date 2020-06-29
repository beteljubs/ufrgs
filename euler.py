# resolução da EDO dx/dt = x para x(0) = 1 pelo Método de Euler Explícito
# solução exata: t = exp(x)

import matplotlib.pyplot as plt
import numpy as np

# função para o método de euler
def f(u):  # dx/dt
    f = u
    return f

# resultado exato da função
def ext(t):
    u = np.exp(t)
    return u

# problema de valor inicial
# dx/dt = x; x(t = 0) = 1
t0 = 0
x0 = 1
xext0 = 1

# valor do passo
h = .0005

tmax = 10000

# listas de valores dos eixos
t = []
x = []
xext = []

tn = t0
xn = x0
xnext = xext0

for i in range (0, tmax):
    # adicionando valores aos vetores
    t.append(tn)
    x.append(xn)
    xext.append(xnext)
    if i == (4 / h):
        print(xn)
    xn += f(xn)*h
    xnext = ext(tn)
    tn += h

# plot dos gráficos
plt.plot(t, x, label = "euler")
plt.plot(t, xext, label = "analítico")
plt.legend()
plt.show()

'''
# print dos valores em um arquivo
arq = open('valores.dat', 'w')

i = 0

for i in range (0, 2000):
    str_u = str(u[i])
    str_u_ext = str(u_ext[i])
    arq.write(str_u + " ")
    arq.write(str_u_ext + "\n")

arq.close()
'''
