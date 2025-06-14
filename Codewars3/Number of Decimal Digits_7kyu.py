"""
Nombre: Addi Toro Chávez.
Fecha: 27 de mayo del 2025.
Descripción:
Determine el número total de dígitos del entero (n > = 0) dado como entrada a la función.
Por ejemplo, 9 tiene un solo dígito,66 tiene 2 dígitos y 128685 tiene 6 dígitos.
Tenga cuidado de evitar desbordamientos o sub desbordamientos.
"""

def digits(n):
    """
    Función que retorna el número de dígitos de un cadena de números.
    """
    return len(str(n))

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(digits(5))
    print(digits(12345))
    print(digits(987654321))
    print(digits(10273))