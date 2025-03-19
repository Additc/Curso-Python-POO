"""
Nombre: Addi Toro Chávez.
Fecha: 19 de marzo del 2025
Descripción:
Es bastante sencillo. Tu objetivo es crear una función que elimine el primer y el último carácter de una cadena.
Se te da un parámetro: la cadena original.
No tienes que preocuparte por cadenas con menos de dos caracteres.
"""


def remove_char(cadena:str)->str:
    """
    Función que devuelve una subcadena de la original,
    comenzando desde el índice 1 (segundo carácter) hasta el índice -1 (penúltimo carácter).
    De esta forma, elimina el primer y el último carácter.
    :param cadena: Cadena de usuario
    :return: Devuleve una subcadena sin el primer y último carácter.
    """
    return cadena[1:-1]

if __name__ == '__main__':
    print(remove_char("eloquent"))
    print(remove_char("country"))
    print(remove_char("person"))
    print(remove_char("place"))
    print(remove_char("OK"))
    print(remove_char("OOOPSSS"))