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

def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia, escala, nivel):
    pila = []
    aTurtle.setheading(90)
    for cmd in instrucciones:
        if cmd == '0':
            aTurtle.color("brown")  # Colorear el tallo marrón
            aTurtle.forward(distancia / escala)  # Reducir la distancia en función de la escala
        elif cmd == '1':
            aTurtle.color("green")  # Colorear las ramas verdes
            aTurtle.forward(distancia / escala)  # Reducir la distancia en función de la escala
        elif cmd == '[':
            pila.append((aTurtle.xcor(), aTurtle.ycor(), aTurtle.heading()))
            aTurtle.left(angulo)
        elif cmd == ']':
            xcor, ycor, heading = pila.pop()
            aTurtle.penup()
            aTurtle.setpos(xcor, ycor)
            aTurtle.pendown()
            aTurtle.setheading(heading)
            aTurtle.right(angulo)
    aTurtle.penup()
def main():
    numRecursions = [0, 1, 2, 3, 4, 7]
    texto = ["Axion", "First", "Second", "third", "fourth", "seventh"]
    angulo = 45
    distancia = 60
    escala = 1
    x = -300    
    tracer(0,0)
    for num in range (len(numRecursions)):
        t = Turtle() # crea la tortuga
        wn = Screen()
        inst = crearSistemaL(numRecursions[num], "0")  # crea la cadena
        print(inst)
        t.up()
        t.setpos(x,-200) # definir la posicion
        t.down()
        t.write(texto[num], align="center", font=("Arial", 12, "normal"))
        t.up()
        t.setpos(x,-180) # definir la posicion
        t.down()
        dibujarSistemaL(t, inst, angulo, distancia, 4, numRecursions[num])
        x+=100
        distancia -=10
    done()

main()
