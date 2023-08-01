# Librerias
import numpy as np
import matplotlib.pyplot as plt

# Modulo para normalizar el vector dado 
def normalizar(vector):
    return vector / np.linalg.norm(vector)

# Modulo para hallar el reflejo aplicando la formula y usando la normal (eje)
def reflejado(vector, eje):
    return vector - 2 * np.dot(vector, eje) * eje

# Modulo para hallar la interseccion entre un rayo y una esfera
def interseccion_esfera(centro, radio, origen_rayo, direccion_rayo):
    # Hallar b que es el producto punto del rayo y su origen menos en centro de la esfera
    b = 2 * np.dot(direccion_rayo, origen_rayo - centro)
    # Hallar c que es la normalizacion del origen del rayo menos el centro de la esfera, todo menos el radio, con ambos valores elevados al cuadrado
    c = np.linalg.norm(origen_rayo - centro) ** 2 - radio ** 2
    # Hallar el valor delta similar a la discriminante en algebra
    delta = b ** 2 - 4 * c
    # Si delta es mayor a 0
    if delta > 0:
        # Hallar ambos valores resultantes de una ecuacion de segundo grado
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        # Si ambos valores son mayores a 0, escoger el menor
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    # Si no se cumple alguna de las anteriores condiciones, no devolver nada
    return None

# Modulo para hallar el objeto (esfera) más cercano y la distancia a la que se encuentre
def objeto_intersectado_mas_cercano(objetos, origen_rayo, direccion_rayo):
    # Hallar las distancias de cada objeto
    distancias = [interseccion_esfera(obj['centro'], obj['radio'], origen_rayo, direccion_rayo) for obj in objetos]
    # Inicializamos la variable que contendra el objeto más cercano y la distancia minima
    objeto_mas_cercano = None
    distancia_minima = np.inf
    # Bucle para buscar el objeto más cercano en la lista de objetos
    for indice, distancia in enumerate(distancias):
        # Si se encuentra una distancia menor, actualizar el valor de la distancia minima y objeto más cercano
        if distancia and distancia < distancia_minima:
            distancia_minima = distancia
            objeto_mas_cercano = objetos[indice]
    # Devolver resultados
    return objeto_mas_cercano, distancia_minima

ancho = 300
altura = 200

profundidad_maxima = 3

# Camara y demás valores para visualizar la imagen
camara = np.array([0, 0, 1])
ratio = float(ancho) / altura
pantalla = (-1, 1 / ratio, 1, -1 / ratio) # izquiera, arriba, derecha, abajo

# Luz con sus parametros
luz = { 'posicion': np.array([5, 5, 5]), 'ambiente': np.array([1, 1, 1]), 'difuso':np.array([1, 1, 1]), 'especular': np.array([1, 1, 1]) }

# Lista con los objetos y sus parametros
objetos = [
    { 'centro': np.array([-0.2, 0, -1]), 'radio': 0.7, 'ambiente': np.array([0.1, 0, 0]),
      'difuso': np.array([0.7, 0, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
    { 'centro': np.array([0.1, -0.3, 0]), 'radio': 0.1, 'ambiente': np.array([0.1, 0, 0.1]),
      'difuso': np.array([0.7, 0, 0.7]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
    { 'centro': np.array([-0.3, 0, 0]), 'radio': 0.15, 'ambiente': np.array([0, 0.1, 0]),
      'difuso': np.array([0, 0.6, 0]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 },
    { 'centro': np.array([0, -9000, 0]), 'radio': 9000 - 0.7, 'ambiente': np.array([0.1, 0.1, 0.1]),
      'difuso': np.array([0.6, 0.6, 0.6]), 'especular': np.array([1, 1, 1]), 'brillo': 100,
      'reflexion': 0.5 }
]

imagen = np.zeros((altura, ancho, 3))
# Crear bucles para evaluar cada punto en la pantalla y asignarle su respectivo color
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
            # Si no hay objetos, salir del bucle for
            if objeto_mas_cercano is None:
                break

            # Hacer uso de los modulos previamente comentados
            interseccion = origen + distancia_minima * direccion
            normal_a_superficie = normalizar(interseccion - objeto_mas_cercano['centro'])
            punto_desplazado = interseccion + 1e-5 * normal_a_superficie
            interseccion_con_luz = normalizar(luz['posicion'] - punto_desplazado)

            _, distancia_minima = objeto_intersectado_mas_cercano(objetos, punto_desplazado, interseccion_con_luz)
            interseccion_con_luz_distancia = np.linalg.norm(luz['posicion'] - interseccion)
            esta_sombreado = distancia_minima < interseccion_con_luz_distancia

            # Si el la distancia minima del objeto más cercano es menor que la interseccion con la luz, salir del bucle for
            if esta_sombreado:
                break
            
            # Crear un array con 3 coordenadas con valor 0
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

# Guardar imagen
plt.imsave('imagen.png', imagen)
# Poner la imagen en el plot
imgplot = plt.imshow(imagen)
# Mostrar el plot
plt.show()
