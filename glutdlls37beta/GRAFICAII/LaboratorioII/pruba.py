import turtle

def generar_cadena(iteraciones):
    axiom = "F++F++F"
    regla = "F-F++F-F"
    cadena = axiom
    
    for _ in range(iteraciones):
        nueva_cadena = ""
        for char in cadena:
            if char == "F":
                nueva_cadena += regla
            else:
                nueva_cadena += char
        cadena = nueva_cadena
    
    return cadena

def dibujar_copo_de_nieve(iteraciones, longitud):
    cadena = generar_cadena(iteraciones)
    
    tortuga = turtle.Turtle()
    pantalla = turtle.Screen()
    pantalla.bgcolor("white")
    
    tortuga.speed(0)
    tortuga.up()
    tortuga.goto(-longitud/2, 0)
    tortuga.down()
    
    for char in cadena:
        if char == "F":
            tortuga.forward(longitud/3)
        elif char == "+":
            tortuga.right(60)
        elif char == "-":
            tortuga.left(60)
    
    turtle.done()

iteraciones = 4
longitud = 400
dibujar_copo_de_nieve(iteraciones, longitud)
