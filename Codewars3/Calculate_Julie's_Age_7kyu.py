"""
Nombre: Addi Toro Chávez.
Fecha: 27 de mayo del 2025.
Descripción:
Julie es x años mayor que su hermano y también y veces mayor que él.
Dados x e y, crea una función que calcule la edad de Julie.
"""

def age(x, y):
    """
    Función que calcula la edad de Julie.
    """
    b = x / (y - 1)
    return b + x


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(age(-15,0.25))
    print(age(6,3))
    print(age(7,2))