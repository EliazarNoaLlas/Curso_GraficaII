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
        nuevaCadena += aplicarReglas(ch)
    return nuevaCadena

def aplicarReglas(ch):
    nuevaCadena = ""
    if ch == '1':
        nuevaCadena = '11'  # Regla 1
    elif ch == '0':
        nuevaCadena = '1[0]0'  # Regla 2
    else:
        nuevaCadena = ch  # No se aplica regla, mantenemos el caracter
    return nuevaCadena

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    pila = []
    for cmd in instrucciones:
        if cmd == '0':
            aTurtle.forward(distancia)
            aTurtle.stamp()  # Dibuja una hoja al final del segmento
        elif cmd == '1':
            aTurtle.forward(distancia)
        elif cmd == '[':
            pila.append((aTurtle.position(), aTurtle.heading()))
            aTurtle.left(angulo)
        elif cmd == ']':
            position, heading = pila.pop()
            aTurtle.penup()
            aTurtle.goto(position)
            aTurtle.setheading(heading)
            aTurtle.pendown()
            aTurtle.right(angulo)

def main():
    inst = crearSistemaL(4, "0")  # crea la cadena
    print(inst)
    t = Turtle()  # crea la tortuga
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(2)
    dibujarSistemaL(t, inst, 45, 40)

main()
