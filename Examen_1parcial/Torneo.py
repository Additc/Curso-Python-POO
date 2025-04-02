"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase Torneo
"""
from Equipo import Equipo
from Jugador import Jugador


class Torneo:
    def __init__(self,nombre:str,*equipos:Equipo):
        self._nombre=nombre
        self._equipos=list(equipos)

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

    def agregar_equipos(self,*equipos:Equipo)->None:
        for equipo in equipos:
            if  equipo._nombre not in self._equipos:
                self._equipos.append(equipo)
            else:
                print("El jugador ya tiene equipo")

    def remover_equipos(self,*equipos:Equipo)->None:
        for equipo in equipos:
            if equipo._nombre in self._equipos:
                self._equipos.remove(equipo)
                print(f" Se eliminó al equipo: {equipo._nombre} correctamente.")
            else:
                print(f"El equipo no existe")

    def mostrar_equipos(self)-> None:
        pass

    def generar_rol(self)->None:
        pass

    def __str__(self) -> str:
        pass

