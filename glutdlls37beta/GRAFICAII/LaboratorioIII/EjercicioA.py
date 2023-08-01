import numpy as np
import matplotlib.pyplot as plt

def normalizar(vector):
    return vector / np.linalg.norm(vector)  # norma del vector

def interseccion_esfera(centro, radio, origen_rayo, direccion_rayo):  # calcular t
    a = np.dot(direccion_rayo, direccion_rayo)  # producto punto
    b = 2 * np.dot(direccion_rayo, origen_rayo - centro)
    c = np.dot(origen_rayo - centro, origen_rayo - centro) - radio ** 2
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / (2 * a)
        t2 = (-b - np.sqrt(delta)) / (2 * a)
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None

def objeto_intersectado_mas_cercano(objetos, origen_rayo, direccion_rayo):
    distancias = [interseccion_esfera(obj['centro'], obj['radio'], origen_rayo, direccion_rayo) for obj in objetos]
    objeto_mas_cercano = None
    distancia_minima = np.inf  # infinito positivo
    for indice, distancia in enumerate(distancias):
        if distancia and distancia < distancia_minima:
            distancia_minima = distancia
            objeto_mas_cercano = objetos[indice]
    return objeto_mas_cercano, distancia_minima

ancho = 300
alto = 200
camara = np.array([0, 0, 1])
proporcion = float(ancho) / alto
pantalla = (-1, 1 / proporcion, 1, -1 / proporcion)  # izquierda, arriba, derecha, abajo

objetos = [
    {'centro': np.array([-0.2, 0, -1]), 'radio': 0.7, 'color': [255, 0, 0]},
    {'centro': np.array([0.1, -0.3, 0]), 'radio': 0.1, 'color': [0, 255, 0]},
    {'centro': np.array([-0.3, 0, 0]), 'radio': 0.15, 'color': [0, 0, 255]}
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
        # computar el punto de intersección entre el rayo y el objeto mas cercano
        interseccion = origen + distancia_minima * direccion
        color = objeto_mas_cercano['color']
        imagen[i, j] = np.clip(color, 0, 255) / 255

    print("%d/%d" % (i + 1, alto))

plt.imsave('imagen.png', imagen)
imgplot = plt.imshow(imagen)
plt.show()
