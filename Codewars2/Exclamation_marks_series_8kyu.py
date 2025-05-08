"""
Nombre: Addi Toro Chávez.
Fecha: 18 de abril del 2025
Descripción:
Reemplace todas las vocales por signos de exclamación en la oración.
aeiouAEIOU es vocal.
"""

def replace_exclamation(st):
    """
    Función que sustituye una vocal por un signo de exclamación.
    """
    cadena=""
    for i in st:
        if i=="a" or i == "e" or i == "i"or i == "o" or i =="u":
            i="!"
            cadena+=i
        elif i=="A" or i == "E" or i == "I"or i == "O" or i =="U":
            i="!"
            cadena+=i
        else:
            cadena+=i
    return cadena

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(replace_exclamation("Hi!"))
    print(replace_exclamation("!Hi! Hi!"))
    print(replace_exclamation("aeiou"))
    print(replace_exclamation("ABCDE"))
