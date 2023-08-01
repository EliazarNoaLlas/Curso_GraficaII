from turtle import *
def crearSistemaL(numIters,axioma):
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
    nuevaCadena = ""
    if ch == '1':
        nuevaCadena = '11' # Regla 1
    elif ch == '0':
        nuevaCadena = '1[0]0' # Regla 2
    else:
        nuevaCadena = ch # No se aplica regla, mantenemos el caracter
    return nuevaCadena

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    pila = []
    aTurtle.setheading(90)
    for cmd in instrucciones:
        if cmd == '0':
            aTurtle.forward(distancia)
        elif cmd == '1':
            aTurtle.forward(distancia)
        elif cmd == '[':
            pila.append((aTurtle.xcor(),aTurtle.ycor(),aTurtle.heading()))
            aTurtle.left(angulo)
        elif cmd == ']':
            xcor, ycor, heading = pila.pop()
            aTurtle.penup()
            aTurtle.setpos(xcor,ycor)
            aTurtle.pendown()
            aTurtle.setheading(heading)
            aTurtle.right(angulo)

def main():
    inst = crearSistemaL(3, "0") # crea la cadena
    print(inst)
    t = Turtle() # crea la tortuga
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(2)
    dibujarSistemaL(t, inst, 45, 40)
    wn.listen()
    wn.mainloop()
    
main()