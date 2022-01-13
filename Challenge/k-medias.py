import numpy as np
import matplotlib.pyplot as plt
  
def distancia(datos, centroides):
    c = []
    for i in datos:
        c.append(np.argmin(np.sum((i.reshape((1,2)) - centroides) ** 2, axis =1)))
    return c

def cercanos(datos, clusters, assigments):
    cen = []
    for c in range(len(clusters)):
        cen.append(np.mean([datos[x] for x in range(len(datos)) if assigments[x] == c], axis=0))
    return cen
        
        
        
x1 = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11]])
print(x1)

centroides = (np.random.normal(size=(2,2))) + np.mean(x1, axis=0).reshape((1,2))
print(centroides)
for i in range(100):
    a = distancia(x1, centroides)
    centroides = cercanos(x1, centroides, a)
    centroides = np.array(centroides)
    
plt.scatter(x1[:,0], x1[:,1], s=150)
plt.scatter(centroides[:,0], centroides[:,1], s=150)
plt.show()






