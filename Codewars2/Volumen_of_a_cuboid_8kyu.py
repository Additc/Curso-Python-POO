"""
Nombre: Addi Toro Chávez.
Fecha: 18 de abril del 2025
Descripción:
Bob necesita una manera rápida de calcular el volumen de un cuboide rectangular con tres valores:
el length, widthy heightde cuboide.
Escriba una función para ayudar a Bob con este cálculo.
"""

def get_volume_of_cuboid(length, width, height):
    """
    Función que calcula el volumen de un cuboide rectangular
    """
    v=length*width*height
    return v


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(get_volume_of_cuboid(1,2,2))
    print(get_volume_of_cuboid(6.3,2,5))
    print(get_volume_of_cuboid(8,4,5,))
    print(get_volume_of_cuboid(6,7,3,))