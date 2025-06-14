"""
Nombre: Addi Toro Chávez.
Fecha: 30 de mayo del 2025.
Descripción:
Completa la solución para que divida la cuerda en pares de dos caracteres.
Si la cadena contiene un número impar de caracteres, entonces debe reemplazar el segundo carácter que falta del par final con un subrayado ('_').
"""

def solution(s):
    """
    Función que divide la cadena en caracteres pares, y las cadenas impares
    agrega el subrayado "_".
    """
    if len(s) % 2 != 0:
        s += "_"

    pares = []

    for i in range(0, len(s), 2):
        par = s[i] + s[i + 1]
        pares.append(par)

    return pares

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(solution('abs'))
    print(solution('abssddef'))
    print(solution('hola'))
    print(solution('adios'))