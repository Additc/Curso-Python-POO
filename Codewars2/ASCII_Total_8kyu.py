"""
Nombre: Addi Toro Chávez.
Fecha: 19 de abril del 2025
Descripción:
Recibirás una cadena y deberás devolver la suma de todos los caracteres como un entero.
La función debe ser capaz de manejar todos los caracteres ASCII imprimibles.
"""

def uni_total(s):
    """
    Función que realiza la suma de su número ASCII de cada carácter.
    """
    return sum(ord(char) for char in s)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(uni_total("a"))
    print(uni_total("aaa"))
    print(uni_total("b"))
    print(uni_total("c"))