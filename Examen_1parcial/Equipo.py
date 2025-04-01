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
        self._jugadores=list(jugadores)
        self._id_equipo = Equipo.no_id
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
    def players(self) ->list:
        return self._jugadores

    #Metodo de acceso set para los jugadores
    @players.setter
    def players(self, jugadores:tuple[Jugador]) -> None:
        self._jugadores = list(jugadores)

    # Metodo de acceso get para id de equipos
    @property
    def ids(self) -> int:
        return self._id_equipo

    # Metodo de acceso set para id de equipos
    @ids.setter
    def ids(self,no_id:int) -> None:
        self._id_equipo=no_id

    def agregar_jugadores(self,*jugadores:tuple[Jugador])->None:
        for jugador in jugadores:
            self._jugadores.append(jugador)

    def remover_jugadores(self,*jugadores:tuple[Jugador])->None:
        pass

    def mostrar_jugadores(self)->None:
        pass

    def total_goles(self)->int:
        pass

    def __str__(self) -> str:
        return f"Equipo( Nombre: {self._nombre} | Número de equipo: {self._id_equipo} | Jugadores: {self._jugadores:})"

if __name__ == '__main__':
    juan=Jugador("juancamanaey",00)
    lobeto=Jugador("botsito32",10)
    cefor=Equipo("Cefor",[])
    print(cefor)
