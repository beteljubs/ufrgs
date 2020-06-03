import matplotlib.pyplot as plt
import numpy as np

pts = 1000 
eixo_x = []
eixo_y0 = []
eixo_y1 = []
x = -5

def taylor_sen(termo, n, x):
    if n % 2 == 0:
        termo +=

for pts in range (0, 100):
    eixo_x.append(x) 
    eixo_y0.append(np.sin(x))
    taylor_sen(termo, pts, x)
    eixo_y1.append(termo)
    x += .1

  

plt.plot(eixo_x, eixo_y)
plt.show()
plt.label("sen")
