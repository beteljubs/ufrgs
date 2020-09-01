# no começo, escolha n entre 0 e 1 para diferentes valores de F (entre 0.0 e 1.0)

'''
Pêndulo simples forçado e amortecido
x' = dx/dt = v
x'' = dv/dt = - c - sin(x) + Fcos(wt)

x = theta               # ângulo
F = torque_ext/mgl      # força
w = raiz(l/g)w_ext      # velocidade angular
t' = t/t0               # tempo adimensional (frequência)
c = b/(ml²w0)           # cte

x0 = 1.0                # ângulo inicial (rad)
v0 = 0.0                # velocidade angular inicial (rad)
c = 0.05
w = 0.7
'''

import matplotlib.pyplot as plt
import numpy as np

def f1(t,x,v):
    f =  v
    return f

def f2(t,x,v):
    f = - c*v - np.sin(x) + Fn*np.cos(w*t)
    return f

# constantes
c = 0.05
w = 0.7
m = 1
g = 9.81
l = 1
T = 2*np.pi/w

h = .01
tmax = 10000
tmin = 400

x_pc = []
v_pc = []
e = .01                 # distancia para o teste de igualdade float
d = 0
i = 0

# valores iniciais
x0 = 1.0                # ângulo inicial (rad)
v0 = 0.0                # velocidade angular inicial (rad)
t0 = 0.0                # tempo inicial

# vetores
x = []
v = []
t = []
F = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

xn = x0
vn = v0
tn = t0

n = -1

while n < 0 or n > 1:
    print('escolha um valor entre 0 e 1 (intervalos de 0.1):')
    n = float(input())

i = int(n*10)
Fn = F[i]

k1x = h*vn
k1v = h*f2(tn,xn,vn)

xm = xn + (1/2)*k1x
vm = vn + (1/2)*k1v

k2x = h*vm
k2v = h*f2(tn + h/2,xm,vm)

xm = xn + k2x/2
vm = vn + k2v/2

k3x = h*vm
k3v = h*f2(tn + h/2,xm,vm)

xm = xn + k3x
vm = vn + k3v

k4x = h*vm
k4v = h*f2(tn+h,xm,vm)

while tn < tmax:
    if tn > 400:        # descarte dos valores iniciais (< 400)
        t.append(tn)
        v.append(vn)

        # limitação dos angulos:
        while xn > np.pi:
            xn = xn - 2*np.pi
        while xn < - np.pi:
            xn = xn + 2*np.pi
        x.append(xn)

    if np.abs(tn - d*T) < 0.01:   # teste de igualdade para Poincare
        if tn > 5000:
            x_pc.append(xn)
            v_pc.append(vn)
        d += 1

    xa = xn
    k1x = h*vn
    k1v = h*f2(tn,xn,vn)
    xm = xn + (1/2)*k1x
    vm = vn + (1/2)*k1v

    k2x = h*vm
    k2v = h*f2(tn + h/2,xm,vm)

    xm = xn + k2x/2
    vm = vn + k2v/2

    k3x = h*vm
    k3v = h*f2(tn + h/2,xm,vm)

    xm = xn + k3x
    vm = vn + k3v

    k4x = h*vm
    k4v = h*f2(tn+h,xm,vm)

    tn += h
    xn = xn + (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
    vn = vn + (1/6)*(k1v + 2*k2v + 2*k3v + k4v)

arq1 = f"F{Fn}_angulo.png"
arq2 = f"F{Fn}_velocidade.png"
arq3 = f"F{Fn}_esp-fase.png"
arq4 = f"F{Fn}_poincare.png"


# plot dos gráficos

title = 'ângulo x tempo'
plt.title(title)

plt.plot(t, x, label = f'F = {Fn}')
plt.xlim(400,500)
plt.ylabel('x')
plt.xlabel('t')
plt.legend()
#plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
#plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
plt.savefig(arq1)
plt.show()

#

title = 'velocidade x tempo'
plt.title(title)

plt.plot(t, v, label = f'F = {Fn}')
plt.ylabel('v')
plt.xlabel('t')
plt.xlim(400,1000)
plt.legend()
#plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
#plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
plt.savefig(arq2)
plt.show()

#

title = 'espaço de fase'
plt.title(title)

plt.scatter(x, v, label = f'F = {Fn}', s = .5)
plt.ylabel('v')
plt.xlabel('x')
plt.legend()
#plt.xlim(-5E-5,5E-5)
#plt.ylim(-5E-5,5E-5)
plt.xlim(-np.pi,np.pi)
plt.ylim(-np.pi,np.pi)
#plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
#plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
plt.savefig(arq3)
plt.show()

#

title = 'diagrama de Poincaré'
plt.title(title)

plt.scatter(x_pc, v_pc, label = f'F = {Fn}', s = .5)
plt.ylabel('v')
plt.xlabel('x')
plt.xlim(-np.pi,np.pi)
plt.ylim(-np.pi,np.pi)
plt.legend()
plt.savefig(arq4)
plt.show()
