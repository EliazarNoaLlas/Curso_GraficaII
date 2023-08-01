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
    distancias = [interseccion_esfera(obj['centro'], obj['radio'], origen_rayo, direccion_rayo) for obj in objetos]
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

camara = np.array([0, 0.8, 3])
ratio = float(ancho) / altura
pantalla = (-1, 1 / ratio, 1, -1 / ratio) # izquiera, arriba, derecha, abajo

luz = { 'posicion': np.array([-1000, 1000, 0]), 'ambiente': np.array([1, 1, 1]), 'difuso':np.array([1, 1, 1]), 'especular': np.array([1, 1, 1]) }

# parámetros
piso = -2
atras = -3
radio1 = 0.5
center = piso + radio1
lejos = 3

objetos = [
    # Objeto 1
    { 'centro': np.array([0.2, center, -1 + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
    # Objeto 2
    { 'centro': np.array([-0.2, center, -1 - lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0, 0.7, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # Objeto 3
    { 'centro': np.array([-0.7, center, -1 - 2*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # Objeto 4
    { 'centro': np.array([-1.1, center, -1 - 3*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0, 0.7, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # Objeto 5
    { 'centro': np.array([-1, center, -1 - lejos/2 + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0.9, 0.9, 0.1]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # Objeto 6
    { 'centro': np.array([-1.4, center, -1 - 3*lejos/2 + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # Objeto 7
    { 'centro': np.array([-2, center, -1 - 5*lejos/2 + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0.7, 0.4, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 8
    { 'centro': np.array([-2.2, center, -1 - 0.9*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0.7, 0.4, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 9
    { 'centro': np.array([0.3, center, -1 - 2.3*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 10
    { 'centro': np.array([0, center, -1 - 4*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 11
    { 'centro': np.array([-1, center, -1 - 6*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 12
    { 'centro': np.array([-2.4, center, -1 - 5*lejos + atras]), 'radio': radio1, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0, 0.7, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
      # objeto 13
    { 'centro': np.array([0, -10000, 0]), 'radio': 10000 + piso, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0.9, 0.9, 0.9]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0 }
]

imagen = np.zeros((altura, ancho, 3))
for i, y in enumerate(np.linspace(pantalla[1], pantalla[3], altura)):
    for j, x in enumerate(np.linspace(pantalla[0], pantalla[2], ancho)):
        # pantalla esta en el origen
        pixel = np.array([x, y, 0])
        origen = camara
        direccion = normalizar(pixel - origen)

        color = np.zeros((3))
        reflexion = 1
        
        for k in range(profundidad_maxima):
            # verifica por intersecciones
            objeto_mas_cercano, distancia_minima = objeto_intersectado_mas_cercano(objetos, origen, direccion)
            if objeto_mas_cercano is None:
                break
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
    
plt.imsave('iluminacion1.png', imagen)
imgplot = plt.imshow(imagen)
plt.show()
