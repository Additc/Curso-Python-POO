"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Ejercicio 2 Scoreboard
"""

class ScoreBoard:
    def __init__(self,points:int=0,text_color:tuple[int,int,int]=(0,0,0), font:str="Kimono",size:float=0):
        self._points=points
        self._text_color= text_color
        self._font=font
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
    @text.setter
    def text(self, text_color:tuple[int])-> None:
        self._text_color= text_color

    # Metodo de acceso get para el font
    @property
    def fonts(self) -> str:
        return self._font

    # Metodo de acceso set para el font
    @fonts.setter
    def fonts(self, font: str) -> None:
        self._font = font

    # Metodo de acceso get para el front
    @property
    def sizes(self) -> float:
        return self._size

    # Metodo de acceso set para el front
    @sizes.setter
    def sizes(self, size: float) -> None:
        self._size = size

    def __str__(self) -> str:
        return f"Scoreboard(Points: {self._points}, Text color:{self._text_color}, Front:{self._font}, Size:{self._size})"


if __name__ == '__main__':
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = ScoreBoard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = ScoreBoard(10, font="Arial", text_color=(127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()