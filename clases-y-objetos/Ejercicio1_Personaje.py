"""
Nombre: Addi Toro Chávez.
Fecha: 12 de marzo del 2025
Descripción:
Ejercicio 1 clase personaje.
"""

class Personaje:
    """
    Clase que representa un personaje.
    Sus atributos son: no_id (atributo de clase).
    Sus métodos son: __init__(), __str__(), moverse(), pocision_actual().
    """
    no_id = 1


    def __init__(self)->None:
        """
        Constructor del Personaje
        """

        self.x = x=0
        self.y = y=0
        self.id_personaje = Personaje.no_id
        Personaje.no_id += 1

    def moverse(self,ordenes:str)->None:
        pass

    def pocision_actual(self)->None:
        pass

    def __str__(self) -> str:
        return f"Profesor nombre: "



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    pass