import numpy as np
import matplotlib.pyplot as plt
def normalizar(vector):
    return vector / np.linalg.norm(vector)
def reflejado(vector, eje):
    return vector - 2 * np.dot(vector, eje) * eje
def interseccion_esfera(centro, radio, origen_rayo, direccion_rayo):
    b = 2 * np.dot(direccion_rayo, origen_rayo - centro)
    c = np.linalg.norm(origen_rayo - centro) ** 2 - radio ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None
def objeto_intersectado_mas_cercano(objetos, origen_rayo, direccion_rayo):
    distancias = [interseccion_esfera(obj['centro'], obj['radio'], origen_rayo,
    direccion_rayo) for obj in objetos]
    objeto_mas_cercano = None
    distancia_minima = np.inf
    for indice, distancia in enumerate(distancias):
        if distancia and distancia < distancia_minima:
            distancia_minima = distancia
            objeto_mas_cercano = objetos[indice]
    return objeto_mas_cercano, distancia_minima
ancho = 300
altura = 200
profundidad_maxima = 3
camara = np.array([0, 0, 1])
ratio = float(ancho) / altura
pantalla = (-1, 1 / ratio, 1, -1 / ratio) # izquiera, arriba, derecha, abajo
luz = { 'posicion': np.array([5, 5, 5]), 'ambiente': np.array([1, 1, 1]), 'difuso':
np.array([1, 1, 1]), 'especular': np.array([1, 1, 1]) }
objetos = [
{ 'centro': np.array([-0.3, 2, -2]), 'radio': 0.20, 'ambiente': np.array([0, 0, 1]),
'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.1 },
{ 'centro': np.array([-0.3, 0.1, 4]), 'radio': 0.20, 'ambiente': np.array([1, 0, 0]),
'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.1 },
{ 'centro': np.array([0.5, 0, 4]), 'radio': 0.20, 'ambiente': np.array([0, 0, 1]),
'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.1 },
{ 'centro': np.array([0.1, -0.3, 0]), 'radio': 0.15, 'ambiente': np.array([0, 0,
1]), 'difuso': np.array([0.7, 0, -4.5]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.1 },
{ 'centro': np.array([0.7, -0.3, 0]), 'radio': 0.20, 'ambiente': np.array([0, 0,
1]), 'difuso': np.array([0.7, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.1 },
{ 'centro': np.array([0.4, -0.4, 0]), 'radio': 0.20, 'ambiente': np.array([1, 0,
0.1]), 'difuso': np.array([0.7, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.3, -0.4, 0]), 'radio': 0.20, 'ambiente': np.array([0, 0, 1]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.2, -0.4, 0.4]), 'radio': 0.10, 'ambiente': np.array([0, 1, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.1, -0.4, 3]), 'radio': 0.10, 'ambiente': np.array([1, 0, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.1, -0.4, 0.3]), 'radio': 1, 'ambiente': np.array([1, 0, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.1, -0.4, -0.3]), 'radio': 0.10, 'ambiente': np.array([0, 1, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-0.7, -0.4, -0.3]), 'radio': 0.15, 'ambiente': np.array([1, 0, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([-1.0, -0.4, -0.5]), 'radio': 0.30, 'ambiente': np.array([0, 1, 0]),
'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
'reflexion': 0.5 },
{ 'centro': np.array([0, -9000, 0]), 'radio': 9000 - 0.7, 'ambiente': np.array([0.1,
0.1, 0.1]), 'difuso': np.array([0.6, 0.6, 0.6]), 'especular': np.array([1, 1, 1]),
'brillo': 100, 'reflexion': 0.5 }
]
#Crea una matriz 3D vacía para almacenar la imagen renderizada, donde alto y ancho son las dimensiones de la imagen.
imagen = np.zeros((altura, ancho, 3))
#El bucle for con enumerate extrae las coordenadas x e y de cada píxel en la ventana gráfica de la pantalla.
for i, y in enumerate(np.linspace(pantalla[1], pantalla[3], altura)):
    for j, x in enumerate(np.linspace(pantalla[0], pantalla[2], ancho)):
        # pantalla esta en el origen
        pixel = np.array([x, y, 0])
        origen = camara
        direccion = normalizar(pixel - origen)
        color = np.zeros((3))
        reflexion = 1
        #este bucle itera a través de cada rayo emitido por la cámara para comprobar las intersecciones con los 
        #objetos de la escena y calcular la iluminación y el sombreado de cada píxel.
        for k in range(profundidad_maxima):
            # verifica por intersecciones
            objeto_mas_cercano, distancia_minima = objeto_intersectado_mas_cercano(objetos, origen, direccion)
            if objeto_mas_cercano is None:
                break
            #La función objeto_intersectado_mas_cercano se utiliza para encontrar el objeto más cercano intersectado por el rayo.
            interseccion = origen + distancia_minima * direccion
            normal_a_superficie = normalizar(interseccion - objeto_mas_cercano['centro'])
            punto_desplazado = interseccion + 1e-5 * normal_a_superficie
            interseccion_con_luz = normalizar(luz['posicion'] - punto_desplazado)
            _, distancia_minima = objeto_intersectado_mas_cercano(objetos, punto_desplazado, interseccion_con_luz)
            interseccion_con_luz_distancia = np.linalg.norm(luz['posicion'] - interseccion)
            esta_sombreado = distancia_minima < interseccion_con_luz_distancia
            if esta_sombreado:
                break
            iluminacion = np.zeros((3))
            # ambiente
            iluminacion += objeto_mas_cercano['ambiente'] * luz['ambiente']
            # difuso
            iluminacion += objeto_mas_cercano['difuso'] * luz['difuso'] * np.dot(interseccion_con_luz, normal_a_superficie)
            # especular
            interseccion_a_camara = normalizar(camara - interseccion)
            H = normalizar(interseccion_con_luz + interseccion_a_camara)
            iluminacion += objeto_mas_cercano['especular'] * luz['especular'] * np.dot(normal_a_superficie, H) ** (objeto_mas_cercano['brillo'] / 4)
            # reflexion
            color += reflexion * iluminacion
            reflexion *= objeto_mas_cercano['reflexion']
            origen = punto_desplazado
            direccion = reflejado(direccion, normal_a_superficie)
        imagen[i, j] = np.clip(color, 0, 1)
    print("%d/%d" % (i + 1, altura))
#Imprime las imagenes 
plt.imsave('imagenB1.png', imagen)
imgplot = plt.imshow(imagen)
plt.show()