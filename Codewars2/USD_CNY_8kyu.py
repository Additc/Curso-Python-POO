"""
Nombre: Addi Toro Chávez.
Fecha: 21 de abril del 2025
Descripción:
Cree una función que convierta dólares estadounidenses (USD) a yuanes chinos (CNY).
La entrada es la cantidad en USD como un entero y la salida debe ser una cadena que indique
la cantidad en yuanes seguida de "Yuan chino".
"""

def usdcny(usd):
    """
    Función que convierte un número de dolares a yuanes chinos.
    """
    tasa_conversion = 6.75
    cny = usd * tasa_conversion
    return f"{cny:.2f} Chinese Yuan"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(usdcny(15))
    print(usdcny(465))
    print(usdcny(25))
    print(usdcny(10))