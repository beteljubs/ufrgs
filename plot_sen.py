import matplotlib.pyplot as plt
import numpy as np

pts = 1000
eixo_x = []
eixo_y = []
x = 0

for pts in range (0, 100):
    eixo_x.append(x)
    eixo_y.append(np.sin(x))
    x += .1

plt.plot(eixo_x, eixo_y)
plt.show()
plt.xlabel("sen")
plt.ylabel("oi")
