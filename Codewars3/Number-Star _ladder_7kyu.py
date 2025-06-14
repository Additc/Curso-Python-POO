"""
Nombre: Addi Toro Chávez.
Fecha: 27 de mayo del 2025.
Descripción:
Usando n como parámetro en la función pattern, dónde n > 0,
complete el código para obtener el patrón
"""


def pattern(n):
    result = ""

    for i in range(1, n + 1):
        line = "1"
        if i > 1:
            stars = '*' * (i - 1)
            line += stars + str(i)
        result += line

        if i != n:
            result += '\n'

    return result


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(pattern(1))
    print(pattern(3))
    print(pattern(7))
    print(pattern(10))