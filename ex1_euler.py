import matplotlib.pyplot as plt
import numpy as np

def f(t, u):  # EDO u'(t) = 1/2u(t) + 2 + t
    u = -.5 * u + 2 + t
    return u

def ext(t):  # calculo do valor exato da EDO (feito na mão)
    u = 2*t + 8* np.exp(-t/2)
    return u

# valores iniciais:
t_n = 0
u_n = 8

# listas para armazenamento dos valores
t = []  # eixo horizontal
u = []  # eixo vertical
u_ext = []  # eixo vertical (valores exatos)

# passo de cada loop
h = .01

# repetir o processo 200 vezes
for i in range (0, 2000):
    # adciona valores na lista
    t.append(t_n)
    u.append(u_n)
    u_ext.append(ext(t_n))
    if t_n > 1.9 and t_n < 2:
        print(u_n)  # print do valor encontrado quando t = 1
    u_n += h * f(t_n, u_n)
    t_n += h  # passo

# plot dos dois gráficos no mesmo arquivo
plt.plot(t, u)
plt.plot(t, u_ext)
plt.show()
