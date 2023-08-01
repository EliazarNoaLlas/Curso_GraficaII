from turtle import *

def crearSistemaL(numIters, axioma):
    cadenaInicio = axioma
    cadenaFin = ""
    if numIters == 0:
        cadenaFin = cadenaInicio
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
    if ch == 'A':
        return 'ABA'
    elif ch == 'B':
        return 'BBB'
    else:
        return ch

def dibujarSistemaL(aTurtle, instrucciones, distancia, grosor):
    aTurtle.width(grosor)
    for cmd in instrucciones:
        if cmd == 'A':
            aTurtle.forward(distancia)
        elif cmd == 'B':
            aTurtle.penup()
            aTurtle.forward(distancia)
            aTurtle.pendown()
    aTurtle.penup()
def main():
    tracer(0,0)
    x= 200
    tamaño = 600
    grosor = 5
    
    for i in range(7):
        inst = crearSistemaL(i, "A") # crea la cadena
        print(inst)
        t = Turtle() # crea la tortuga
        wn = Screen()
        t.up()
        t.setpos(-300,x)
        t.down()
        t.speed(0)
        
        t.width(2)
        dibujarSistemaL(t, inst, tamaño,grosor)
        x -=50
        tamaño = tamaño/3
        grosor = grosor/2
    done()
main()
