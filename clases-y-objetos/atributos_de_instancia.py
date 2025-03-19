"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Clases
"""

class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre  # Hacemos que forme parte del objeto
        self.temas_aprendidos = []

    def aprender_tema(self,tema:str)->None:
        self.temas_aprendidos.append(tema) # aniadimos un tema a lista de ese objeto
        print(f"{self.nombre} aprendió {tema}")

    #Método mágico
    def __str__(self)->str:
        return f"Estudiante nombre:{self.nombre} Temas aprendidos: {self.temas_aprendidos} "

class Profesor:
    def __init__(self, nombre: str,temas_dominados:list[str]):
        self.nombre = nombre  # Hacemos que forme parte del objeto
        self.temas_dominados = temas_dominados

    def dominar_tema(self,tema: str)-> None:
        self.temas_dominados.append(tema)  # aniadimos un tema a lista de ese objeto
        print(f"EL profesor {self.nombre} domina el tema: {tema}")

    def enseniar_tema(self,no_tema:int)->str:
        if no_tema < len(self.temas_dominados): #Válidamos temas
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"

    # Método mágico
    def __str__(self) -> str:
        return f"Profesor nombre:{self.nombre} Temas dominados: {self.temas_dominados} "


#Objetos
if __name__=="__main__":
    estudiante1=Estudiante("Addi")
    estudiante2=Estudiante("Alberto")

    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("Internet de las cosas")
    print()
    print(estudiante1)
    print(estudiante2)
    print()

    #Ahora para la class profesor
    profesor1=Profesor("Alberto",["matemáticas","Programación","Futbol"])
    print(profesor1)

    print(profesor1.enseniar_tema(0))
    print()
#Relacionando objetos
    estudiante1.aprender_tema(profesor1.enseniar_tema(1))
    estudiante2.aprender_tema(profesor1.enseniar_tema(2))

