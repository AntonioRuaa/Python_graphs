import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cts
import math as m

#Defines el grid sobre el que se va a graficar
u = np.linspace(-1, 1, 10)
v = np.linspace(-5, 5, 10)
w = np.linspace(-1, 1, 10)
U, V, W = np.meshgrid(u, v, w)

#Defines la función vectorial
# u => x ; y => v ; z => w
def r(u, v, w):
  n = 1
  x = 0
  y = 0
  z = 0
  while n < 20:  #Sumatoria
    x = x + m.exp(-1*v)*u*m.cos(w)
    y = y + m.exp(u)*m.sin(w)
    z = z + w
    n = n+1
  return x, y, z

#Definimos las variables y graficamos

r_vec = np.vectorize(r)
X, Y, Z = r_vec(U, V, W)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(U, V, W, X, Y, Z, length=0.01)

#Nombre de gráfica y ejes
ax.set_title('Campo Vectorial en 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()