"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase Equipo
"""
from duplicity.commandline import select_files

from Jugador import Jugador


class Equipo:
    no_id = 1
    def __init__(self,nombre:str,*jugadores:Jugador):
        self._nombre=nombre
        self._jugadores=list(jugadores)
        self._id_equipo = Equipo.no_id
        Equipo.no_id += 1

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def agregar_jugadores(self,*jugadores:Jugador)->None:
        for jugador in jugadores:
            if jugador.nombres not in self._jugadores:
                self._jugadores.append(jugador)
            else:
                print("El jugador ya tiene equipo")

    def remover_jugadores(self,*jugadores:Jugador)->None:
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
                print(f" Se eliminó al jugador: {jugador.nombres} correctamente.")
            else:
                print(f"El jugador no existe")

    def mostrar_jugadores(self)->None:
        for i, item in enumerate (self._jugadores):
            print(f"{i+1}.{item}")


    def total_goles(self)->int:
        total_goles = sum(jugador._goles for jugador in self._jugadores)
        return total_goles

    def __str__(self) -> str:
        nombres = [jugador.nombres for jugador in self._jugadores]
        return f"Equipo: {self._nombre} | Número de equipo: {self._id_equipo} | Jugadores: {nombres}"


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

