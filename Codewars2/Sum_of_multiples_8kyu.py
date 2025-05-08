"""
Nombre: Addi Toro Chávez.
Fecha: 24 de abril del 2025
Descripción:
Calcula la suma de todos los múltiplos de n menores que m.
Recuerda:
n y m son números naturales (enteros positivos).
m se excluye de los múltiplos.
"""

def sum_mul(n, m):
    """
    Función que obtiene la suma de los múltiplos de un número b, hasta
    un número final m.
    """
    if n <= 0 or m <= 0:
        return "INVALID"
    k = (m - 1) // n
    total_sum = n * k * (k + 1) // 2
    return total_sum


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(sum_mul(2,9))
    print(sum_mul(3, 13))
    print(sum_mul(4, 123))
    print(sum_mul(4, -7))