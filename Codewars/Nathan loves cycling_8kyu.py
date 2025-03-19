"""
Nombre: Addi Toro Chávez.
Fecha: 12 de marzo del 2025
Descripción:
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
"""


def litres(time):
    """
    Función que calcula el tiempo en litros que Nathan a consumido.
    :param time: Tiempo el que a practicado ciclismo.
    :return: Cantidad de litros en entero que a bebido.
    """
    litros=0.5*time
    return int(litros)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(litres(0))
    print(litres(1))
    print(litres(2))
    print(litres(3))
    print(litres(4))
