"""
Nombre: Addi Toro Chávez.
Fecha: 13 de abril del 2025
Descripción:
Tienes que crear una función calcType, que recibe 3 argumentos: 2 números,
y el resultado de una operación desconocida realizada en ellos (también un número).
Basado en esos 3 valores tienes que devolver una cadena, que describe qué operación se utilizó
para obtener el resultado dado.
Las posibles cuerdas de retorno son: "addition", "subtraction", "multiplication", "division".
"""

def calc_type(a, b, resultado):
    """
    Función que verifica la operación aritmética que se está utilizando,
    para obtener el resultado.
    """
    #Comparaciones correspondientes
    if a + b == resultado:
        return "addition"
    elif a - b == resultado:
        return "subtraction"
    elif a * b == resultado:
        return "multiplication"
    elif b != 0 and a / b == resultado:
        return "division"
    else:
        return "operación desconocida"

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(calc_type(1,2,3))
    print(calc_type(10,5,5))
    print(calc_type(10,4,40))
    print(calc_type(9,5,1.8))