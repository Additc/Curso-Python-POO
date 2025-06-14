"""
Nombre: Addi Toro Chávez.
Fecha: 30 de mayo del 2025.
Descripción:
Termina la solución para que tome una entrada n (entero)
y devuelva una cadena que sea la representación decimal del número agrupado por comas
después de cada 3 dígitos.
"""

def group_by_commas(n):
    """
    Función que agrupa un número n con , después de 3 dígitos.
    """
    num_str = str(n)
    resultado = ''
    contador = 0

    for i in range(len(num_str) - 1, -1, -1):
        resultado = num_str[i] + resultado
        contador += 1
        if contador == 3 and i != 0:
            resultado = ',' + resultado
            contador = 0

    return resultado

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(group_by_commas(1))
    print(group_by_commas(10))
    print(group_by_commas(100))
    print(group_by_commas(1000))
    print(group_by_commas(10000))
    print(group_by_commas(100000))