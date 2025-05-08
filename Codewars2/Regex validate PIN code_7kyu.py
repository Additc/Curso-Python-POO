"""
Nombre: Addi Toro Chávez.
Fecha: 13 de abril del 2025
Descripción:
Los cajeros automáticos permiten códigos PIN de 4 o 6 dígitos y
los códigos PIN no pueden contener nada más que exactamente 4 dígitos o exactamente 6 dígitos.
Si la función se pasa una cadena PIN válida, devuelva true, de lo contrario volver false.
"""

def validate_pin(pin):
    """
    Función que válida que un pin sean exactamente 4 o 6 dígitos.
    """
    return pin.isdigit() and len(pin) in (4, 6)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(validate_pin("12345"))
    print(validate_pin("1234"))
    print(validate_pin("a234"))
    print(validate_pin("123456"))