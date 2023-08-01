def es_primo(n):
    """
    Verifica si un número es primo.

    Args:
        n (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    num_numeros = int(input("Ingrese la cantidad de números: "))
    numeros_primos = []
    numeros_compuestos = []
    for _ in range(num_numeros):
        num = int(input("Ingrese un número: "))
        if es_primo(num):
            numeros_primos.append(num)
        else:
            numeros_compuestos.append(num)

    promedio_primos = sum(numeros_primos) / len(numeros_primos) if numeros_primos else 0
    promedio_compuestos = sum(numeros_compuestos) / len(numeros_compuestos) if numeros_compuestos else 0

    print("Números primos:", numeros_primos)
    print("Números compuestos:", numeros_compuestos)
    print("El promedio de todos los números primos es", promedio_primos)
    print("El promedio de todos los números compuestos es", promedio_compuestos)

main()
