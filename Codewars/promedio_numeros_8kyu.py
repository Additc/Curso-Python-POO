"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Escribe una función que calcule el promedio de los números en un array dado.
Nota: Los arrays vacíos deben devolver 0.
"""


def find_average(numbers):
    """
    Funcón para calcular el promedio de números de un array determinado.
    :param numbers: Array de números.
    :return: El total del promedio en dado caso que si tenga número dentro, en caso contrario será 0.
    """
    suma = 0
    if len(numbers) == 0:
        return 0
    else:
        for i in numbers:
            suma += i
        total = suma / len(numbers)
        return total

if __name__ == '__main__':
    print(find_average([1,2,3]))
    print(find_average([]))
    print(find_average([1,2]))
