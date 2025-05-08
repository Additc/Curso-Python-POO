"""
Nombre: Addi Toro Chávez.
Fecha: 20 de abril del 2025
Descripción:
Tu tarea consiste en crear una función que realice cuatro operaciones matemáticas básicas.
La función debe aceptar tres argumentos: operación(cadena/carácter), valor1(número), valor2(número).
La función debe devolver el resultado de números después de aplicar la operación elegida.
"""

def basic_op(operator, value1, value2):
    """
    Función que obtiene el resultado de la operación aritmetica a realizar según sea el operador.
    """
    if operator == "+":
        return value1+value2
    elif operator == "-":
        return value1-value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        return value1/value2


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(basic_op("+",4,7))
    print(basic_op("-", 15, 18))
    print(basic_op("*", 5, 5))
    print(basic_op("/", 49, 7))