"""
Nombre: Addi Toro Chávez.
Fecha: 27 de mayo del 2025.
Descripción:
Escriba una función que encuentre la suma de todos sus argumentos.
"""

def sum_args(*args):
    """
    Función que muestra la suma de todos los argumentos.
    """
    return sum(args)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(sum_args(1,2))
    print(sum_args(5, 7,9))
    print(sum_args(12, 1,1,1,1))
    print(sum_args(1, 23))