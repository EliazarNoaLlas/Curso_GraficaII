import re

def gramatica_valores(initial_string):
    pattern = r'~(\d+(?:\.\d+)?) : (.*?)\s*(?=\||\})'
    matches = re.findall(pattern, initial_string)
    values_dict = {}
    for match in matches:
        key = match[1].strip()
        value = float(match[0]) if '.' in match[0] else int(match[0])
        values_dict[key] = value
    return values_dict 

def cubo(altura, ancho_x, ancho_z, x, z):
    vertices = []
    vertices.extend([(-ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, altura, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, 0, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])

    vertices.extend([(ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, altura, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])

    vertices.extend([(-ancho_x/2)+x, altura, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, altura, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, altura, (ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (ancho_z/2)+z, 0.0, 0.0])

    vertices.extend([(-ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, 0, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(-ancho_x/2)+x, altura, (-ancho_z/2)+z, 0.0, 0.0])
    vertices.extend([(ancho_x/2)+x, 0, (-ancho_z/2)+z, 0.0, 0.0])
    
    return vertices

def triangulo(altura, ancho, x, y, z):
    vertices = []
    a1,a2,a3 = z,0,0
    c = ancho/2
    for i in range(8):
        if i == 4:
            a1,a2,a3 = z,0,0
        a2 = a1 - c
        a3 = a1 - 2*c
        if i < 4:
            vertices.extend([-x, y, a1, 0.0, 0.0])
            vertices.extend([-x, y+altura, a2, 0.0, 0.0])
            vertices.extend([-x, y, a3, 0.0, 0.0])
        else:
            vertices.extend([x, y, a1, 0.0, 0.0])
            vertices.extend([x, y+altura, a2, 0.0, 0.0])
            vertices.extend([x, y, a3, 0.0, 0.0])
        a1 = a3
    return vertices

def triangulo2(altura, ancho, x, y, z):
    vertices = []
    a1,a2,a3 = x,0,0
    c = ancho/2
    for i in range(6):
        if i == 3:
            a1,a2,a3 = x,0,0
        a2 = a1 - c
        a3 = a1 - 2*c
        if i < 3:
            vertices.extend([a1, y, z, 0.0, 0.0])
            vertices.extend([a2, y+altura, z, 0.0, 0.0])
            vertices.extend([a3, y, z, 0.0, 0.0])
        else:
            vertices.extend([a1, y, z-(ancho*4), 0.0, 0.0])
            vertices.extend([a2, y+altura, z-(ancho*4), 0.0, 0.0])
            vertices.extend([a3, y, z-(ancho*4), 0.0, 0.0])
        a1 = a3
    return vertices

def invertir(altura, ancho, x, y, z):
    vertices = []
    a1,a2,a3 = z,0,0
    c = ancho/2
    for i in range(8):
        if i == 4:
            a1,a2,a3 = z,0,0
        a2 = a1 - c
        a3 = a1 - 2*c
        if i < 4:
            vertices.extend([-x, y+altura, a1, 0.0, 0.0])
            vertices.extend([-x, y, a2, 0.0, 0.0])
            vertices.extend([-x, y+altura, a3, 0.0, 0.0])
        else:
            vertices.extend([x, y+altura, a1, 0.0, 0.0])
            vertices.extend([x, y, a2, 0.0, 0.0])
            vertices.extend([x, y+altura, a3, 0.0, 0.0])
        a1 = a3
    return vertices

def invertir2(altura, ancho, x, y, z):
    vertices = []
    a1,a2,a3 = x,0,0
    c = ancho/2
    for i in range(6):
        if i == 3:
            a1,a2,a3 = x,0,0
        a2 = a1 - c
        a3 = a1 - 2*c
        if i < 3:
            vertices.extend([a1, y+altura, z, 0.0, 0.0])
            vertices.extend([a2, y, z, 0.0, 0.0])
            vertices.extend([a3, y+altura, z, 0.0, 0.0])
        else:
            vertices.extend([a1, y+altura, z-(ancho*4), 0.0, 0.0])
            vertices.extend([a2, y, z-(ancho*4), 0.0, 0.0])
            vertices.extend([a3, y+altura, z-(ancho*4), 0.0, 0.0])
        a1 = a3
    return vertices

def open_arreglo(file_path):
    strings_array = []
    with open(file_path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            strings_array.append(clean_line)
    return strings_array


#initial_string = ["lote --> cubo(1) { ~10 : altura | ~20 : ancho(x) | ~20.0 : ancho(z) } centro(xy) {~0 : x | ~0 : z}","lote --> cubo(1) { ~15 : altura | ~12 : ancho(x) | ~16 : ancho(z)} centro(xy) {~0 : x | ~2 : z}"]
initial_string = open_arreglo('D:/Python/Computacion Grafica 2/Torre/gramatica.txt')
#print(initial_string)
vertices = []
for i in initial_string:
    if 'cubo' in i:
        dic = gramatica_valores(i)
        if 'repetir' in i:
            p = i.index('repetir')
            print(p)
            al = dic['altura']
            for i in range(2):
                vertices += cubo(al, dic['ancho(x)'], dic['ancho(z)'], dic['x'], dic['z'])
                al += dic['altura']
        else:
            dic = gramatica_valores(i)
            vertices += cubo(dic['altura'], dic['ancho(x)'], dic['ancho(z)'], dic['x'], dic['z'])
    elif 'invertir(4)' in i:
        dic = gramatica_valores(i)
        vertices += invertir(dic['altura'], dic['ancho'], dic['x'], dic['y'], dic['z'])

    elif 'invertir(3)' in i:
        dic = gramatica_valores(i)
        vertices += invertir2(dic['altura'], dic['ancho'], dic['x'], dic['y'], dic['z'])

    elif 'triangulo(4)' in i:
        dic = gramatica_valores(i)
        vertices += triangulo(dic['altura'], dic['ancho'], dic['x'], dic['y'], dic['z'])

    elif 'triangulo(3)' in i:
        dic = gramatica_valores(i)
        vertices += triangulo2(dic['altura'], dic['ancho'], dic['x'], dic['y'], dic['z'])

#print(dic)

nombre_archivo = "D:/Python/Computacion Grafica 2/Torre/puntos.txt"

# Abrir el archivo en modo escritura y escribir los datos
with open(nombre_archivo, "w") as archivo:
    for indice in vertices:
        archivo.write(str(indice) + " ")

