"""
Nombre: Addi Toro Chávez.
Fecha: 28 de marzo del 2025
Descripción:
Necesitamos una función que pueda transformar un número (entero) en una cadena.
¿Qué maneras conoces para lograr esto?
Ejemplos (entrada->salida):
"""

def number_to_string(num):
    """
    Función que convierte un número a cadena
    """
    cadena=str(num)
    return cadena

if __name__ == '__main__':
    print(number_to_string(67))
    print(number_to_string(79585))
    print(number_to_string(-79585))
    print(number_to_string(1+2))
    print(number_to_string(1-2))
