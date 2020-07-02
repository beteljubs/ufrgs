'''
ATIVIDADE PÊNDULO SIMPLES PELOS MÉTODOS:
- Euler Explícito
- Euler Cromer
- Verlet
- Velocity-Verlet

falta plot em escala log
'''
import matplotlib.pyplot as plt
import numpy as np

def f1(theta, vel):  # dtheta/dt = w
    f = vel  # velocidade angular
    return f

def f2(vel, theta):  # dw/dt = a
    f = k*np.sin(theta)
    return f

def Ep(theta):  # energia potencial gravitacional
    dy = L*(1-np.cos(theta))  # altura da massa do pendulo
    E = m * g * dy
    return E

def Ec(theta,vel):  # energia cinética
    v = f1(theta,vel) * L  # velocidade da massa do pêndulo
    E = (1/2)*m *v*v
    return E

# valores iniciais
vel0 = 0  # velocidade
dt = 0.01  # intervalo de tempo
x0 = 1.5  # angulo
t0 = 0  # tempo
tmax = 2000

g = 10
L = 1
k = -g/L
m = 1

E0 = np.abs(Ec(x0,vel0) + Ep(x0))

# Euler Explícito

t = t0
theta = x0
vel = vel0

xee = []
wee = []
tee = []
Eee = []

for i in range (0,tmax):
    thetanovo = theta + f1(theta, vel)*dt
    velnova = vel + f2(vel, theta)*dt
    tee.append(t)
    wee.append(vel)
    xee.append(theta)
    E = Ec(theta,vel) + Ep(theta)
    Em = np.abs(E-E0)/E0
    Eee.append(Em)
    theta = thetanovo
    vel = velnova
    t += dt

# Euler Cromer

t = t0
theta = x0
vel = vel0

xec = []
wec = []
tec = []
Eec = []

for i in range (0, tmax):
    velnova = vel + f2(vel, theta)*dt
    thetanovo = theta + f1(theta, velnova)*dt
    tec.append(t)
    wec.append(vel)
    xec.append(theta)
    E = Ec(theta,vel) + Ep(theta)
    Em = np.abs(E-E0)/E0
    Eec.append(Em)
    vel = velnova
    theta = thetanovo
    t += dt

# Verlet

t = t0
theta = x0
vel = vel0

thetaa = theta + vel*dt + .5* f2(vel,theta) *dt*dt

xv = []
wv = []
tv = []
Ev = []

for i in range (0,tmax):
    xv.append(theta)
    tv.append(t)
    thetap = 2*theta - thetaa + f2(vel,theta) *dt*dt
    thetaa = theta
    theta = thetap
    t += dt

# Velocity-Verlet

t = t0
theta = x0
vel = vel0
acc = f2(vel,theta)

xvv = []
wvv = []
tvv = []
Evv = []

for i in range (0,tmax):
    xvv.append(theta)
    tvv.append(t)
    wvv.append(acc)
    acc = f2(vel,theta)
    E = Ec(theta,vel) + Ep(theta)
    Em = np.abs(E-E0)/E0
    Evv.append(Em)
    theta = theta + vel*dt + .5* acc *dt*dt
    vel = vel + (dt/2) * (acc + f2(vel,theta))
    t += dt

# PLOTS:

lble = "euler"
lblec = "euler-cromer"
lblv = "verlet"
lblvv = "velocity-verlet"

'''
title = "posição"
plt.plot(tee, xee, label=lble)
plt.plot(tec, xec, label=lblec)
plt.plot(tv, xv, label=lblv)
plt.plot(tvv, xvv, label=lblvv)
plt.legend()
plt.title(title)
plt.show()

title = "velocidade angular"
plt.plot(tee, wee, label=lble)
plt.plot(tec, wec, label=lblec)
plt.plot(tvv, wvv, label=lblvv)
plt.legend()
plt.legend(title)
plt.show()rung

title = "energia"
plt.plot(tee, Eee, label=lble)
plt.plot(tec, Eec, label=lblec)
plt.plot(tvv, Evv, label=lblvv)
plt.legend()
plt.show()
'''

title = "energia - escala log"
plt.plot(tee, Eee, label=lble)
plt.plot(tec, Eec, label=lblec)
plt.plot(tvv, Evv, label=lblvv)
plt.yscale('log')
plt.xlim(0)
plt.legend()
plt.show()
