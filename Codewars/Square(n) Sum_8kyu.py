"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Ejercicio de una suma de números dados con exponenciación.
"""

def square_sum(numbers):
    """
    Función que recibe una lista de números y realiza la suma de cada uno de ellos elevandos al cuadrado.
    :param numbers: Lista de números.
    :return: El total de la suma.
    """
    suma = 0
    total = 0
    for i in numbers:
        suma = (i ** 2)
        total = total + suma
    print(total)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    square_sum([1,2])
    square_sum([0, 3, 4, 5])
    square_sum([])
    square_sum([-1,-2])
    square_sum([-1,0,1])
