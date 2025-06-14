"""
Nombre: Addi Toro Chávez.
Fecha: 30 de mayo del 2025.
Descripción:
Dado n, se calcula la suma de los dígitos de n.
Si ese valor tiene más de un dígito, se continúa reduciendo de esta manera
hasta obtener un número de un solo dígito. La entrada será un entero no negativo.
"""

def digital_root(n):
    """
    Función que calcula la suma de n números dados.
    """
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(digital_root(123))
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(456))