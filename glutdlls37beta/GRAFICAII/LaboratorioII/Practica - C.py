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
    if ch == 'F':
        
        nuevaCadena = 'F+F-F-FF+F+F-F' # Regla 1
    else:
        nuevaCadena = ch # No se aplica regla, mantenemos el caracter
    return nuevaCadena
def dibujarSistemaL(aTurtle, instrucciones, angulo, distancia):
    aTurtle.color("blue")
    for cmd in instrucciones:
        if cmd == 'F':
            aTurtle.forward(distancia)
        elif cmd == '+':  
            aTurtle.left(angulo)
        elif cmd == '-':
            aTurtle.right(angulo)
def main():
    tracer(0, 0)
    inst = crearSistemaL(2, "F+F+F+F") # crea la cadena
    print(inst)
    t = Turtle() # crea la tortuga
    wn = Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    dibujarSistemaL(t, inst, 90, 5) # dibuja la imagen
    # angulo 60, longitud de segmento 5
    done()
main()
