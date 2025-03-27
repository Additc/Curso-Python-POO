"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase Equipo
"""
from Jugador import Jugador


class Equipo:
    no_id = 1
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        self._nombre=nombre
        self._jugadores=jugadores

        self.id_equipo = Equipo.no_id
        Equipo.no_id += 1

    # Metodo de acceso get para nombre de equipos

    @property
    def equipos(self) ->str:
        return self._nombre

    #Metodo de acceso set para nombre de equipos
    @equipos.setter
    def equipos(self, nombre:str) -> None:
        self._nombre = nombre

    # Metodo de acceso get para los jugadores

    @property
    def players(self) ->tuple:
        return self._jugadores

    #Metodo de acceso set para los jugadores
    @players.setter
    def players(self, jugadores:tuple[Jugador]) -> None:
        self._jugadores = jugadores
