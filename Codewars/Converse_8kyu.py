"""
Nombre: Addi Toro Chávez.
Fecha: 27 de marzo del 2025
Descripción:
Dado un número aleatorio no negativo,
debes devolver los dígitos de este número dentro de una matriz en orden inverso.
"""


def digitize(n):
    """
    Función que verifica que los números sean positivos y los retorna en una lista
    de manera inversa.
    :param n: Cojunto de números
    :return: Lista de números invertidos
    """
    resultado = []
    while n > 0:
        resultado.append(n % 10)  # Extrae el último dígito
        n //= 10  # Elimina el último dígito
    return resultado if resultado else [0]  # Maneja el caso de número = 0



if __name__ == '__main__':
    print(digitize(35231))
    print(digitize(0))
    print(digitize(23582357))
    print(digitize(984764738))
    print(digitize(45762893920))
