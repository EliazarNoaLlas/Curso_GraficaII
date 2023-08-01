def encontrar_mcm(num1, num2, num3):
    """
    Encuentra el mínimo común múltiplo de 3 números.

    Args:
        num1 (int): El primer número.
        num2 (int): El segundo número.
        num3 (int): El tercer número.

    Returns:
        int: El mínimo común múltiplo de los 3 números.
    """

    mcm = num1
    while not (mcm % num2 == 0 and mcm % num3 == 0):
        mcm += 1
    return mcm

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    mcm = encontrar_mcm(num1, num2, num3)
    print("El mínimo común múltiplo de los 3 números es", mcm)
main()
