# Lançamento Obliquo pelo método de Runge-Kutta de 4a ordem para mecânica
# comparação com o método de velocity-verlet e RK2 (ponto médio)

import numpy as np
import matplotlib.pyplot as plt

def accx(x,v):
    a = - gamma*v
    return a

def accy(y,v):
    a = -g -gamma*v
    return a

# constantes
g = 9.81
gmm = [0.0, 0.005, 0.01, 0.02, 0.04, 0.08]
theta = np.deg2rad(60)

# valores iniciais
x0 = 0
y0 = 0
v0 = 600
vx0 = v0*np.cos(theta)
vy0 = v0*np.sin(theta)

t0 = 0
tmax = 150

h = .01

# vetores

x4 = []
y4 = []
t4 = []

n = 0

while n < 6:
    gamma = gmm[n]

    x4.clear()
    y4.clear()
    t4.clear()

    vxn = vx0
    vyn = vy0
    xn = x0
    yn = y0
    tn = t0

    k1x = h*vxn
    k1vx = h*accx(xn,vxn)
    k1y = h*vyn
    k1vy = h*accy(yn,vyn)

    xm = xn + (1/2)*k1x
    vxm = vxn + (1/2)*k1vx
    ym = yn + (1/2)*k1y
    vym = vyn + (1/2)*k1vy

    k2x = h*vxm
    k2vx = h*accx(xm, vxm)
    k2y = h*vym
    k2vy = h*accy(ym, vym)

    xm = xn + (1/2)*k2x
    vxm = vxn + (1/2)*k2vx
    ym = yn + (1/2)*k2y
    vym = vyn + (1/2)*k2vy

    k3x = h*vxm
    k3vx = h*accx(xm, vxm)
    k3y = h*vym
    k3vy = h*accy(ym, vym)

    xm = xn + k3x
    vxm = vxn + k3vx
    ym = yn + k3x
    vym = vyn + k3vy

    k4x = h*vxm
    k4vx = h*accx(xm, vxm)
    k4y = h*vym
    k4vy = h*accy(ym, vym)

    while tn < tmax:
        t4.append(tn)
        x4.append(xn)
        y4.append(yn)

        k1x = h*vxn
        k1vx = h*accx(xn,vxn)
        k1y = h*vyn
        k1vy = h*accy(yn,vyn)

        xm = xn + (1/2)*k1x
        vxm = vxn + (1/2)*k1vx
        ym = yn + (1/2)*k1y
        vym = vyn + (1/2)*k1vy

        k2x = h*vxm
        k2vx = h*accx(xm, vxm)
        k2y = h*vym
        k2vy = h*accy(ym, vym)

        xm = xn + (1/2)*k2x
        vxm = vxn + (1/2)*k2vx
        ym = yn + (1/2)*k2y
        vym = vyn + (1/2)*k2vy

        k3x = h*vxm
        k3vx = h*accx(xm, vxm)
        k3y = h*vym
        k3vy = h*accy(ym, vym)

        xm = xn + k3x
        vxm = vxn + k3vx
        ym = yn + k3y
        vym = vyn + k3vy

        k4x = h*vxm
        k4vx = h*accx(xm, vxm)
        k4y = h*vym
        k4vy = h*accy(ym, vym)

        tn += h
        xn = xn + (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
        vxn = vxn + (1/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
        yn = yn + (1/6)*(k1y + 2*k2y + 2*k3y + k4y)
        vyn = vyn + (1/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)
        axn = accx(xn,vxn)
        ayn = accy(yn,vyn)

    # plots:

    plt.plot(x4,y4, label = rf'$\gamma: {gamma}$')

    n += 1


plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.ylim(bottom=0)
plt.show()
