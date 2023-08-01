import turtle
from turtle import *

def crearSistemaL(numIters, axioma):
    cadenaInicio = axioma
    cadenaFin = ""
    for i in range(numIters):
        cadenaFin = procesarCadena(cadenaInicio)
        cadenaInicio = cadenaFin
    return cadenaFin

def procesarCadena(cadenaVieja):
    nuevaCadena = ""
    for ch in cadenaVieja:
        nuevaCadena = nuevaCadena + aplicarReglas(ch)
    return nuevaCadena

def aplicarReglas(ch):
    if ch == 'F':
        return 'F-G+F+G-F'
    elif ch == 'G':
        return 'GG'
    else:
        return ch

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    aTurtle.setheading(90)
    for cmd in instrucciones:
        if cmd == 'F' or cmd == 'G':
            aTurtle.forward(distancia)
        elif cmd == '+':
            aTurtle.left(angulo)
        elif cmd == '-':
            aTurtle.right(angulo)

def main():
    texto = ["n=2", "n=4", "n=6"]
    iteraciones = [2, 4, 6]
    distancias = [20, 5, 2]
    angulo = 120
    
    turtle.tracer(0, 0)  # Desactivar la animación
    for i in range(len(iteraciones)):
        inst = crearSistemaL(iteraciones[i], "F-G-G")
        print(inst)
        
        t = Turtle()
        wn = Screen()
        wn.setworldcoordinates(-200, -200, 200, 200)  # Establecer el sistema de coordenadas de dibujo
        t.up()
        t.setpos(-150 + i * 120, -20) # definir la posicion
        t.down()
        t.write(texto[i], align="center", font=("Arial", 12, "normal"))
        t.up()
        t.setpos(-200 + i * 120, 0)
        t.left(60)  # Girar la tortuga en sentido antihorario
        t.down()
        t.speed(0)
        t.width(1)
        dibujarSistemaL(t, inst, angulo, distancias[i])
    
    done()

main()
