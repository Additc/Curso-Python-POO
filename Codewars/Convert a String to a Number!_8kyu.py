"""
Nombre: Addi Toro Chávez.
Fecha: 28 de marzo del 2025
Descripción:
Necesitamos una función que pueda transformar una cadena en un número.
¿Qué maneras conoces de lograrlo?
Nota: No te preocupes, todas las entradas serán cadenas,
y cada cadena es una representación perfectamente válida de un número entero.
"""

def string_to_number(s):
    """
    Función que convierte una cadena, a un número entero mediante la
    instrucción (int).
    """
    numero=int(s)
    return numero

if __name__ == '__main__':
    print(string_to_number("1234"))
    print(string_to_number("605"))
    print(string_to_number("1405"))
    print(string_to_number("-7"))
    print(string_to_number("0"))