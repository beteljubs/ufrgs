import matplotlib.pyplot as plt
import numpy as np

N0 = float(1000)  # num de atomos inicial
a = float(9.24*(10**(-3)))  # coef. de decaimento radioativo
eixo_Nu = []
eixo_t = []
eixo_Nulog = []

# 1. integrar a equacao do decaimento radioativo usando o metodo de Euler exp

for t in range(0, 120):
    N0 -= a*N0
    eixo_Nu.append(N0)
    eixo_t.append(t)
    eixo_Nulog.append(np.log(N0))
    if t == 75:
        print(N0)
    
plt.plot(eixo_t, eixo_Nu)
plt.show()

plt.plot(eixo_t, eixo_Nulog)
plt.show()

# 2. usar os mesmos parametros e integrar usando o método de Euler imp