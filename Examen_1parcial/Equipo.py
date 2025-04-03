"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase Equipo
"""
from duplicity.commandline import select_files

from Jugador import Jugador


""" %%%%%%%%%%%%%%%%     CLASE    %%%%%%%%%%%%%%%%%%%%% """
class Equipo:
    """
    Constructor para inicializar los atributos de la clase equipo.
    """
    no_id = 1
    def __init__(self,nombre:str,*jugadores:Jugador):
        self._nombre=nombre
        self._jugadores=list(jugadores)
        self._id_equipo = Equipo.no_id
        Equipo.no_id += 1

# %%%%%%%%%%%%%%%  MÉTODOS DE ACCESO  %%%%%%%%%%%%%%%%%%
    #Metodo de acceso get para nombre de equipos
    @property
    def equipos(self) ->str:
        return self._nombre

    #Metodo de acceso set para nombre de equipos
    @equipos.setter
    def equipos(self, nombre:str) -> None:
        self._nombre = nombre


    @property
    def integrantes(self) -> list[Jugador]:
        return self._jugadores[:]

    @integrantes.setter
    def integrantes(self, value: list[Jugador]) -> None:
        self._jugadores = list(value)

    # Metodo de acceso get para id de equipos
    @property
    def ids(self) -> int:
        return self._id_equipo

#%%%%%%%%%%%%%%%%%%%%  MÉTODOS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def agregar_jugadores(self,*jugadores:Jugador)->None:
        """
        Métod0 para agregar múltiples jugadores a un equipo.
        """
        for jugador in jugadores:
            if jugador.nombres not in self._jugadores:
                self._jugadores.append(jugador)
            else:
                print("El jugador ya tiene equipo")

    def remover_jugadores(self, *jugadores: Jugador) -> None:
        """
        Métod0 para remover múltiples jugadores de un equipo.
        """
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
                print(f"Se eliminó al jugador: {jugador.nombres} correctamente.")
            else:
                print(f"El jugador {jugador.nombres} no existe en el equipo.")

    def mostrar_jugadores(self)->None:
        """
        Métod0 para mostrar la lista de jugadores.
        """
        for i, item in enumerate (self._jugadores):
            print(f"{i+1}.{item}")


    def total_goles(self)->int:
        """
        Métod0 para calcular el total de goles anotados por todos
        los jugadores del equipo.
        """
        total_goles = sum(jugador._goles for jugador in self._jugadores)
        return total_goles

    def __str__(self) -> str:
        """
        Métod0 mágico para mostrar la información de la clase equipo.
        """
        nombres = [jugador.nombres for jugador in self._jugadores]
        return f"Equipo( Nombre: {self._nombre} | Número de equipo: {self._id_equipo} | Jugadores: {nombres})"


""" %%%%%%%%%%%%%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    juan=Jugador("juancamanaey",11)
    lobeto=Jugador("botsito32",10)
    lobeto.anotar_goles(10)
    cefor=Equipo("Cefor",juan,lobeto)
    print(cefor)
    cefor.mostrar_jugadores()
    print()

    cefor.remover_jugadores(juan)
    print()
    print(cefor)
    print()
    goles=cefor.total_goles()
    print(f"El total de goles del equipo son: {goles} goles")

