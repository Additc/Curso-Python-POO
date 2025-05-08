"""
Nombre: Addi Toro Chávez.
Fecha: 24 de abril del 2025
Descripción:
Los niños beben ponche.
Los adolescentes beben Coca-Cola.
Los adultos jóvenes beben cerveza.
Los adultos beben whisky.

Crea una función que reciba la edad y devuelva lo que beben.
Reglas:
Niños menores de 14 años.
Adolescentes menores de 18 años.
Jóvenes menores de 21 años.
Adultos mayores de 21 años.
"""

def people_with_age_drink(age):
    """
    Función que verifica la edad y la bebida que pueden consumir de acuerdo a ella.
    """
    if age <14:
        return "drink toddy"
    if age <18:
        return "drink coke"
    if age < 21:
        return "drink beer"
    if age >= 21:
        return "drink whisky"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(people_with_age_drink(13))
    print(people_with_age_drink(17))
    print(people_with_age_drink(18))
    print(people_with_age_drink(20))
    print(people_with_age_drink(30))