import numpy as np
import matplotlib.pyplot as plt

def normalizar(vector):
    return vector / np.linalg.norm(vector) #norma del vector

def interseccion_triangulo(vertice0, vertice1, vertice2, origen_rayo, direccion_rayo):
    EPSILON = 0.0000001
    EDGE1 = vertice1 - vertice0
    EDGE2 = vertice2 - vertice0
    H = np.cross(direccion_rayo,EDGE2)
    A = np.dot(EDGE1, H)
    if ( A > -1 * EPSILON and A < EPSILON):
        return None
    F = 1.0 / A
    S = origen_rayo - vertice0
    U = F * (np.dot(S,H))
    if (U < 0.0 or U > 1.0):
        return None
    Q = np.cross(S,EDGE1)
    V = F * np.dot(direccion_rayo,Q)
    if (V < 0.0 or U + V > 1.0):
        return None
    T = F * np.dot(EDGE2,Q)
    if (T > EPSILON):
        print(T)
        return T

def objeto_intersectado_mas_cercano(objetos, origen_rayo, direccion_rayo):
    distancias = [interseccion_triangulo(obj['vertice0'], obj['vertice1'], obj['vertice2'], origen_rayo, direccion_rayo) for obj in objetos]
    objeto_mas_cercano = None
    distancia_minima = np.inf #infinito positivo
    for indice, distancia in enumerate(distancias):
        if distancia and distancia < distancia_minima:
            distancia_minima = distancia
            objeto_mas_cercano = objetos[indice]
    return objeto_mas_cercano, distancia_minima
    
ancho = 300
alto = 200

camara = np.array([0, 0, 1])
proporcion = float(ancho) / alto
pantalla = (-1, 1 / proporcion, 1, -1 / proporcion) # izquierda, arriba, derecha, abajo

objetos = [
{ 'vertice0': np.array([-0.43, 0.01, -1]), 
  'vertice1': np.array([0.69, -0.82, -1]), 
  'vertice2': np.array([1.5, 0.31, -1]), 
  'color': [255, 0, 0] },
{ 'vertice0': np.array([-0.43, 0.01, -1]), 
  'vertice1': np.array([0.38, 1.14, -1]), 
  'vertice2': np.array([1.5, 0.31, -1]), 
  'color': [255, 0, 0] },
{ 'vertice0': np.array([0.69, -0.82, -1]), 
  'vertice1': np.array([0.97, -0.77, -1]), 
  'vertice2': np.array([1.77, 0.36, -1]), 
  'color': [0, 255, 0] },
{ 'vertice0': np.array([0.69, -0.82, -1]), 
  'vertice1': np.array([1.5, 0.31, -1]), 
  'vertice2': np.array([1.77, 0.36, -1]), 
  'color': [0, 255, 0] },
{ 'vertice0': np.array([0.38, 1.14, -1]), 
  'vertice1': np.array([1.5, 0.31, -1]), 
  'vertice2': np.array([1.77, 0.36, -1]), 
  'color': [0, 0, 255] },
{ 'vertice0': np.array([0.38, 1.14, -1]), 
  'vertice1': np.array([0.65, 1.19, -1]), 
  'vertice2': np.array([1.77, 0.36, -1]), 
  'color': [0, 0, 255] }
]

imagen = np.zeros((alto, ancho, 3))
for i, y in enumerate(np.linspace(pantalla[1], pantalla[3], alto)):
    for j, x in enumerate(np.linspace(pantalla[0], pantalla[2], ancho)):
        pixel = np.array([x, y, 0])
        origen = camara
        direccion = normalizar(pixel - origen)
        # chequear por intersecciones
        objeto_mas_cercano, distancia_minima = objeto_intersectado_mas_cercano(objetos, origen, direccion)
        if objeto_mas_cercano is None:
            continue
        # computar el punto de intereseccion entre el rayo y el objeto mas cercano
        interseccion = origen + distancia_minima * direccion
        color = objeto_mas_cercano['color']
        imagen[i, j] = np.clip(color, 0, 1)
        print("%d/%d" % (i + 1, alto))
plt.imsave('imagen.png', imagen)
imgplot = plt.imshow(imagen)
plt.show()