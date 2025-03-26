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
        self._scoreboard=scoreboard

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
        return f"Scoreboard(Title: {self._title}, Width:{self._width}, Heigth:{self._heigth}, Scoreboard:{self._scoreboard})"

if __name__ == '__main__':
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)

    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = ScoreBoard(10, (40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)

    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")