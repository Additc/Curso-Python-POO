"""
Nombre: Addi Toro Chávez.
Fecha: 19 de marzo del 2025
Descripción:
Necesita crear una calculadora sencilla que devuelva el resultado de la suma, resta, multiplicación o
división de dos números.
Su función aceptará tres argumentos:
El primer y el segundo argumento deben ser números.
El tercer argumento debe representar un signo que indique la operación a realizar con estos dos números.
Si las variables no son números o el signo no pertenece a la lista anterior, se devolverá el mensaje "valor desconocido".
"""

def calculator(num1, num2, operacion):
    """
    Función que calcula una operación aritmética de dos números si estos si lo son,según sea el signo,en dado caso que no
    sea uno de los predefinidos regresa valor desconocido.
    """
    # Verificamos que num1 y num2 sean números
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "unknown value"

    # Verificamos que la operación sea una de las permitidas
    if operacion not in ["+", "-", "*", "/"]:
        return "unknown value"

    # Realizamos la operación correspondiente
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        # Evitamos la división por cero
        if num2 == 0:
            return "No se puede dividir entre cero"
        return num1 / num2

if __name__ == '__main__':
    print(calculator(6, 2, '+'))
    print(calculator(4,3,"-"))
    print(calculator(6, '$', '+'))
    print(calculator(6,2,"&"))