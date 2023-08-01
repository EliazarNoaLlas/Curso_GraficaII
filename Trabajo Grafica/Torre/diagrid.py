import re

initial_string = ["lote --> cubo(1) { ~10 : altura | ~20 : ancho(x) | ~20.0 : ancho(z) } centro(xy) {~0 : x | ~0 : z} repetir(2)","lote --> cubo(1) { ~15 : altura | ~12 : ancho(x) | ~16 : ancho(z)} centro(xy) {~0 : x | ~2 : z}"]
for i in initial_string:
    print('---', len(i))
    if 'cubo' in i:
        p = i[i.find('repetir')+8:i.find('repetir')+9]
        print(p)


for i in initial_string:
    print('---', len(i))
    if 'cubo' in i and 'repetir' in i:
        match = re.search(r'repetir\((\d+)\)', i)
        if match:
            p = match.group(1)
            print(p)
            e = int(p)
            print(e)
        else:
            print("No se encontró el número después de 'repetir' en la cadena.")
    else:
        print("No se encontró 'cubo' o 'repetir' en la cadena.")