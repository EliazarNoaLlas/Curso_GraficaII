''''
NOMBRE      : Eliazar Noa Llasccanao
EJERCICIO   : El siguiente programa dibuja la  simulacion de la 
              curva de bezier
              para cualquer cantidad de puntos 
              a continuacion se muestra algunos casos de prueba:
              -  La primera linea es el numero  de puntos n
              -  las siguientes n lineas son las cordenadas 

3
-100 58
-70 189
145 74

4
-70 62
-70 189
161 193
155 71

'''
from turtle import *
import math

def bezier_curve(t, control_points):
    # Calcula un punto en la curva de Bezier para un valor de parámetro t
    n = len(control_points) - 1
    result = Vec2D(0, 0)
    for i, point in enumerate(control_points):
        result += math.comb(n, i) * (1 - t)**(n - i) * t**i * point
    return result

# Obtener puntos de control de la curva de Bezier
# por ejemplo 
control_points = []
nropuntos = int(input())
for _ in range(nropuntos):
    px, py = map(float, input().split())
    control_points.append(Vec2D(px, py))

# Configuración de la tortuga
tortuga = Turtle()
tortuga.penup()

# Dibujar los puntos de control
for i, punto in enumerate(control_points):
    tortuga.goto(punto)
    tortuga.dot()
    if i != len(control_points) - 1:
        tortuga.pendown()
        tortuga.goto(control_points[i + 1])
        tortuga.penup()

tortuga.goto(control_points[0])  # Movimiento a la primera posición sin trazar línea

tortuga.pendown()
t = 0

while t <= 1:
    # Calcular la posición de la curva de Bezier en el valor de parámetro t
    puntos_control = [bezier_curve(t, control_points[i:]) for i in range(len(control_points))]
    posicion = bezier_curve(t, puntos_control)
    tortuga.setheading(tortuga.towards(posicion))
    tortuga.goto(posicion)

    # Calcular la tangente a la curva en el punto actual
    derivada = bezier_curve(t, puntos_control[1:]) - bezier_curve(t, puntos_control[:-1])
    tangente = posicion + derivada

    # Dibujar la recta tangente
    tortuga.penup()
    tortuga.goto(posicion)
    tortuga.pendown()
    tortuga.goto(tangente)

    t += 0.01

screen = Screen()
screen.exitonclick()
