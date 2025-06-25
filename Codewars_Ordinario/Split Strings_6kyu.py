"""
Nombre: Addi Toro Chávez.
Fecha: 24 de junio del 2025.
Descripción:
Complete la solución para que divida la cadena en pares de dos caracteres.
 Si la cadena contiene un número impar de caracteres, debe reemplazar el segundo carácter
faltante del último par con un guion bajo ('_').
"""


def solution(s):
    # Si la longitud de la cadena es impar, se le agrega un guion bajo al final
    if len(s) % 2 != 0:
        s += "_"

    # Se crea una lista vacía para guardar los pares de caracteres
    pares = []

    # Se recorre la cadena de dos en dos
    for i in range(0, len(s), 2):
        # Se forma un par con el carácter actual y el siguiente
        par = s[i] + s[i + 1]
        # Se agrega el par a la lista
        pares.append(par)

        # Se retorna la lista con los pares de caracteres
    return pares


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(solution("hola"))
    print(solution("adios"))
    print(solution("pal"))

