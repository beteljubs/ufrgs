# resolução da EDO dx/dt = x para x(0) = 1 pelo Método de Euler Implícito
# solução exata: t = exp(x)

import matplotlib.pyplot as plt
import numpy as np

# função para o método de euler
def f(u):
    f = u
    return f

# resultado exato da função
def ext(t):
    u = np.exp(t)
    return u

# valor do passo
h = .0005

# problema de valor inicial
# dx/dt = x; x(t = 0) = 1
t_n = 0
u_n = 1
u_n_ext = 1

unovo = u_n / (1 - h)

# listas de valores dos eixos
t = []
u = []
u_ext = []

for i in range (0, 10000):
    # adicionando valores aos vetores
    t.append(t_n)
    u.append(f(u_n))
    u_ext.append(ext(t_n))
    if i == (4 / h):
        print(u_n)
    t_n += h
    u_n = unovo
    unovo = u_n/(1-h)
    unovo = u_n + f(unovo)*h

'''
    # atualizando os valores
    t_n += h
    uaux = u_n
    u_n = unovo
    unovo = uaux + f(unovo)*h
'''
# plot dos gráficos
plt.plot(t, u)
plt.plot(t, u_ext)
plt.show()

'''
# print dos valores em um arquivo
arq = open('valoresi.dat', 'w')

i = 0

for i in range (0, 2000):
    str_u = str(u[i])
    str_u_ext = str(u_ext[i])
    arq.write(str_u + " ")
    arq.write(str_u_ext + "\n")

arq.close()
'''
