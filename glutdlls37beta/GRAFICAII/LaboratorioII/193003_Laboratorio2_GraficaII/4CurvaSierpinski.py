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
    if ch == 'A':
        return 'B-A-B'
    elif ch == 'B':
        return 'A+B+A'
    else:
        return ch

def dibujarSistemaL(aTurtle, instrucciones, longitud, angulo):
    aTurtle.color("blue")  # Colorear 
    for cmd in instrucciones:
        if cmd == 'A' or cmd == 'B':
            aTurtle.forward(longitud)
        elif cmd == '+':
            aTurtle.left(angulo)
        elif cmd == '-':
            aTurtle.right(angulo)
        else:
            aTurtle.penup()

def main():
    iteraciones = [2, 4, 6, 8]
    matriz = [[None, None], [None, None]]
    x = -300
    y = 200
    distancia = 10
    angulo = 60
    texto = ["n=2", "n=4", "n=6", "n=8"]
    turtle.tracer(0, 0)  # Desactivar la animación
    for i in range(2):
        for j in range(2):
            inst = crearSistemaL(iteraciones[i*2+j], "A")
            print(iteraciones[i*2+j])
            print(inst)
            
            t = turtle.Turtle()
            t.speed(0)
            t.width(1)
            t.penup()
            t.goto(x, y)
            t.pendown()
            dibujarSistemaL(t, inst, distancia, angulo)
            t.penup()
            t.goto(x, y - 20)  # Posición para el texto
            t.pendown()
            t.write(texto[i*2+j], align="center", font=("Arial", 12, "normal"))
            
            matriz[i][j] = t
            distancia /=2
            
            x += 300
        x = -300
        y -=300

    
    turtle.done()
main()
