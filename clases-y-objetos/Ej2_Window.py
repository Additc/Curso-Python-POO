"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Ejercicio 2 Window
"""

from Ej2_Scoreboard import ScoreBoard

class Window:
    def __init__(self,title:str,width:int, heigth:int,scoreboard:ScoreBoard=ScoreBoard()):
        self._title=title
        self._width= width
        self._heigth=heigth
        self.scoreboard=scoreboard

    def draw_scoreboard(self)->None:
        pass

    def update_score(self,points:int)->None:
        pass

    # Metodo de acceso get title
    @property
    def titles(self) -> str:
        return self._title

    # Metodo de acceso set title
    @titles.setter
    def titles(self, title: str) -> None:
        self._title = title

    # Metodo de acceso get width
    @property
    def widths(self) -> int:
        return self._width

    # Metodo de acceso set para los puntos
    @widths.setter
    def widths(self, width: int) -> None:
        self._width = width

    # Metodo de acceso get heigth
    @property
    def heig(self) -> int:
        return self._heigth

    # Metodo de acceso set para los puntos
    @heig.setter
    def heig(self, heigth: int) -> None:
        self._heigth = heigth

    # Metodo de acceso get scoreboard
    @property
    def score(self) -> ScoreBoard:
        return self._scoreboard

    # Metodo de acceso set scoreboard
    @score.setter
    def score(self, scoreboard) -> None:
        self._scoreboard = scoreboard

    def __str__(self) -> str:
        pass

if __name__ == '__main__':
    pass