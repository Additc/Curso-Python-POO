"""
Nombre: Addi Toro Chávez.
Fecha: 25 de marzo del 2025
Descripción:
Escriba una función que acepte un entero no negativo n y una cadena s como parámetros,
y devuelva una cadena de s repetida exactamente n veces.
"""

def repeat_str(repeat, string):
    """
    Función que recibe un número de repeticiones y una cadena, retorna la cadena
    el número de veces a repetir.
    """
    return repeat*string

if __name__ == '__main__':
    print(repeat_str(4,"a"))
    print(repeat_str(3, "hello"))
    print(repeat_str(2, "abc"))
    print(repeat_str(0, ""))