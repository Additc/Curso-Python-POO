"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase Torneo
"""
from Equipo import Equipo
from Jugador import Jugador


""" %%%%%%%%%%%%%%%%     CLASE    %%%%%%%%%%%%%%%%%%%%% """
class Torneo:
    def __init__(self,nombre:str,*equipos:Equipo):
        self._nombre=nombre
        self._equipos=list(equipos)

#%%%%%%%%%%%%%%%  MÉTODOS DE ACCESO  %%%%%%%%%%%%%%%%%%

    # Metodo de acceso get para nombre del Torneo
    @property
    def torneos(self) ->str:
        return self._nombre

    #Metodo de acceso set para nombre del Torneo
    @torneos.setter
    def torneos(self, nombre:str) -> None:
        self._nombre = nombre

    # Metodo de acceso get para equipos
    @property
    def equipo(self)->list:
        return self._equipos

    #Metodo de acceso set para equipos
    @equipo.setter
    def equipo(self, *equipos:Equipo) -> None:
        self._equipos = list(equipos)

#%%%%%%%%%%%%%%%%%%%%  MÉTODOS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def agregar_equipos(self,*equipos:Equipo)->None:
        """
        Métod0 para agregar múltiples equipos al torneo.
        """
        for equipo in equipos:
            if  equipo not in self._equipos:
                self._equipos.append(equipo)
            else:
                print("El equipo ya existe")

    def remover_equipos(self,*equipos:Equipo)->None:
        """
        Métod0 para eliminar múltiples equipos al torneo.
        """
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
                print(f"Se eliminó al equipo: {equipo._nombre} correctamente.")
            else:
                print(f"El equipo {equipo._nombre} no existe en el equipo.")

    def mostrar_equipos(self)-> None:
        """
        Métod0 para mostrar la lista de equipos dentro del torneo.
        """
        for i, item in enumerate (self._equipos):
            print(f"{i+1}.{item._nombre}")

    def generar_rol(self)->None:
        """
        Métod0 para generar un rol de partidos "todos contra todos",
        organizados en jornadas.
        """
        if len(self._equipos) < 2:
            print("No existen eqipos suficientes.")
            return

        jornadas = []
        equipos = self._equipos.copy()

        num_jornadas = len(equipos) - 1
        for i in range(num_jornadas):
            partidos = []

            for j in range(len(equipos) // 2):
                partidos.append((equipos[j], equipos[-(j + 1)]))
            jornadas.append(partidos)
            equipos.insert(1, equipos.pop())  # Rotar equipos

        # Mostrar jornadas
        for i, jornada in enumerate(jornadas, start=1):
            print(f"Jornada {i}:")
            for partido in jornada:
                print(f" - {partido[0]._nombre} vs {partido[1]._nombre}")
            print()
        print()

    def __str__(self) -> str:
        """
        Métod0 mágico para mostrar la información de la clase Torneo.
         """
        nombres = [equipo._nombre for equipo in self._equipos]
        return f"Torneo(Nombre: {self._nombre} | Equipos: {nombres})"

if __name__ == '__main__':
    champions=Torneo("Champions league")
    print(champions)
