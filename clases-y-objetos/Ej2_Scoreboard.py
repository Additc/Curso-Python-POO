"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Ejercicio 2 Scoreboard
"""

class ScoreBoard:
    def __init__(self,points:int=0,text_color:tuple[int]=(0,0,0), front:str="Kimono",size:float=0):
        self._points=points
        self._text_color= text_color
        self._front=front
        self._size=size


    def draw(self)->None:
        pass

    # Metodo de acceso get para los puntos

    @property
    def puntos(self) -> int:
        return self._points

    # Metodo de acceso set para los puntos
    @puntos.setter
    def puntos(self, points:int) -> None:
        self._points = points

    # Metodo de acceso get para el texto de color

    @property
    def text(self) -> tuple:
        return self._text_color

    # Metodo de acceso set para el texto de color
    @texter
