"""
Nombre: Addi Toro Chávez.
Fecha: 23 de Junio del 2025.
Descripción:
It's time for some array exchange! The objective is simple: exchange the elements of two arrays
in-place in a way that their new content is also reversed. The arrays may be of unequal lengths,
 in which case you will have to expand the shorter one in-place.
"""

def exchange_with(a, b):
    # Invertir copias de ambas listas
    reversed_a = a[::-1]
    reversed_b = b[::-1]

    # Reasignar totalmente el contenido
    a[:] = reversed_b
    b[:] = reversed_a

    return a, b

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(exchange_with([1,2,3,4,5,6],[9,8,7,6,5,4,3,2,1]))
    print(exchange_with([3,2,1,], ["a","b","c","d"]))