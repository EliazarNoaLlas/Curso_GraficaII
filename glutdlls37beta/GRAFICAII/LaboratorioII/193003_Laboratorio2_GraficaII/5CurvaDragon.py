import turtle

def crearSistemaL(numIters, axioma):
    cadenaInicio = axioma
    cadenaFin = ""
    for _ in range(numIters):
        cadenaFin = procesarCadena(cadenaInicio)
        cadenaInicio = cadenaFin
    return cadenaFin

def procesarCadena(cadenaVieja):
    nuevaCadena = ""
    for ch in cadenaVieja:
        nuevaCadena += aplicarReglas(ch)
    return nuevaCadena

def aplicarReglas(ch):
    if ch == 'F':
        return 'F+G'
    elif ch == 'G':
        return 'F-G'
    else:
        return ch

def dibujarSistemaL(aTurtle, instrucciones, longitud):
    aTurtle.color("blue")  # Colorear
    aTurtle.setheading(90)
    for cmd in instrucciones:
        if cmd == 'F' or cmd == 'G':
            aTurtle.forward(longitud)
        elif cmd == '+':
            aTurtle.left(90)
        elif cmd == '-':
            aTurtle.right(90)
        else:
            aTurtle.penup()

def main():
    iteraciones = 10
    longitud_segmento = 10
    
    inst = crearSistemaL(iteraciones, "F")
    print(inst)
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(1)
    t.penup()
    t.goto(100, 0)
    t.pendown()
    turtle.tracer(0, 0)  # Desactivar la animación
    dibujarSistemaL(t, inst, longitud_segmento)
    
    # Agregar texto
    t.penup()
    t.goto(100, -200)  # Posición para el texto
    t.pendown()
    t.write("Curva del Dragón", align="center", font=("Arial", 16, "bold"))
    turtle.done()

main()
