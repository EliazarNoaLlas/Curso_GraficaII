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
    aTurtle.setheading(90) # orientacion de la tortuga hacia arriba
    for cmd in instrucciones:
        # si cmd es 0 O 1 mueve hacia adelante
        if cmd == '0':
            aTurtle.forward(distancia)
        elif cmd == '1':
            aTurtle.forward(distancia)
        # si cmd es '[' 
        elif cmd == '[':
            # Se guarda la posición actual(coordenada x,y,angulo)
            pila.append((aTurtle.xcor(),aTurtle.ycor(),aTurtle.heading()))
            # gira a al izquierda
            aTurtle.left(angulo)
        # si cmd es ']'
        elif cmd == ']':
            # se obtiene la ultima posicion
            xcor, ycor, heading = pila.pop()
            # se elvnata el lapiz
            aTurtle.penup()
            # se establece la posicion de la tortuga guardada
            aTurtle.setpos(xcor,ycor)
            # se baja el lapiz d ela tortuga
            aTurtle.pendown()
            # se establece el angulo guardado
            aTurtle.setheading(heading)
            # gira a la derecha un angulo
            aTurtle.right(angulo)
def main():
    tracer(0,0)
    inst = crearSistemaL(3, "0") # generar instruccion
    print(inst)
    t = Turtle() # crea la instancia tortuga
    wn = Screen()
    # mover hacia atraz 200 u
    t.up() 
    t.setpos(0,-200)
    t.down()
    t.speed(2) # velocidad
    dibujarSistemaL(t, inst, 45, 40)
    done()
main()
