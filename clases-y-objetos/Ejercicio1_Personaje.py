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
    contador_id = 1


    def __init__(self)->None:
        """
        Constructor del Personaje
        """

        self.x = x=0
        self.y = y=0
        self.id_personaje = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self,ordenes:str)->None:
        """
        Función que verifica los movimientos del personaje.
        """
        for i in ordenes:
            if i == "a" and self.y < 10:
                self.y+=1
            elif i == "r" and self.y > 0:
                self.y-=1
            elif i == "d" and self.x < 10:
                self.x+=1
            elif i == "i" and self.x > 0:
                self.x-=1



    def pocision_actual(self)->None:
        """
        Función que muestra la pocisión actual del personaje.
        """
        print(f"pocisión actual del personaje {self.id_personaje}: (x,y): ({self.x, self.y})")

    def __str__(self) -> str:
        return f"Profesor nombre: "

def solicitar_datos( )->str:
    """
    Función que solicita los movimientos al usuario.
    """
    print()
    print("--Se solicita iterativamente las secuencias de movimiento")
    ordenes = input("Ingrese las órdenes de movimiento: "). lower()
    while  ordenes.isnumeric():
        print("Opción no válida")
        ordenes= input("Intenta nuevamente las órdenes de movimiento: ").lower()
    ordenes = str(ordenes)
    print()
    return  ordenes





""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    personaje1=Personaje()
    while True:
        ordenes = solicitar_datos()
        if ordenes == "s":
            personaje1.pocision_actual()
            print("Fin del programa.")
            break
        personaje1.moverse(ordenes)
        personaje1.pocision_actual()
