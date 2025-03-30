"""
Nombre: Addi Toro Chávez.
Fecha: 30 de marzo del 2025
Descripción:
Bienvenido. En esta kata, se le pide que eleve al cuadrado cada dígito de un número
y los concatene.
"""

def square_digits(num):
    """
    Función que retorna una cadena de número, elevado cada uno al
    cuadrado.
    """
    num_str = str(num)  # Convertir el número a string
    resultado = ""  # Inicializar un string vacío para almacenar el resultado
    for digito in num_str:  # Iterar sobre cada dígito del número
        resultado += str(int(digito) ** 2)  # Elevar al cuadrado y añadir al resultado
    return int(resultado)  # Convertir el resultado concatenado a un número

if __name__ == '__main__':
    print(square_digits(9119))
    print(square_digits(0))
    print(square_digits(523))