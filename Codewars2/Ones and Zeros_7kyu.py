"""
Nombre: Addi Toro Chávez.
Fecha: 11 de abril del 2025
Descripción:
Dado una serie de unos y ceros, convertir el valor binario equivalente a un entero.
Eg: [0, 0, 0, 1]se trata como 0001 que es la representación binaria de 1.
"""

def binary_array_to_number(arr):
    """
    Función que convierte un número binario a decimal.
    """

    #Se convierte el arreglo a una cadena de texto y se unen los elementos en una sola
    #cadena y se convierte el número a decimal usando la base 2.
    return int(''.join(map(str, arr)), 2)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(binary_array_to_number([1, 0, 1]))
    print(binary_array_to_number([0, 0, 0, 1]))
    print(binary_array_to_number([1, 1, 1, 1]))
