"""
Nombre: Addi Toro Chávez.
Fecha: 11 de abril del 2025
Descripción:
Implementar la función que debe volver true si se da objeto es una vocal
 (es decir, a, e, i, o, u, mayúscula o minúscula), y false de otra manera.
"""


def is_vowel(c):
    """
    Función que determina si existe solo una vocal en la cadena.
    """
    #Se convierte la cadena a minúscula y se compara con las vocales y si existe 1.
    return c.lower() in 'aeiou' and len(c) == 1


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(is_vowel(""))
    print(is_vowel("a"))
    print(is_vowel("E"))
    print(is_vowel("eu"))
    print(is_vowel("Z"))