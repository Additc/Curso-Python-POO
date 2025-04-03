"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Clase jugador
"""

""" %%%%%%%%%%%%%%%%     CLASE    %%%%%%%%%%%%%%%%%%%%% """
class Jugador:
    #Constructor de la clase jugador
    def __init__(self,nombre:str,numero:int,goles:int=0):
        self._nombre=nombre
        self._numero=numero
        self._goles=goles

# %%%%%%%%%%%%%%%  MÉTODOS DE ACCESO  %%%%%%%%%%%%%%%%%%
    # Metodo de acceso get para los nombres
    @property
    def nombres(self) -> str:
        return self._nombre

    # Metodo de acceso set para los nombres
    @nombres.setter
    def nombres(self, nombre:str) -> None:
        self._nombre = nombre


    # Metodo de acceso get para número del jugador
    @property
    def numeros(self) -> int:
        return self._numero

    # Metodo de acceso set para número del jugador
    @numeros.setter
    def numeros(self, numero:int) -> None:
        self._numero = numero

    # Metodo de acceso get para los goles
    @property
    def goals(self) -> int:
        return self._goles

    # Metodo de acceso set para los goles
    @goals.setter
    def goals(self, goles:int) -> None:
        self._goles = goles

#%%%%%%%%%%%%%%%%%%%%  MÉTODOS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def anotar_goles(self,no_goles:int)->None:
        """
        Función que incrementar la cantidad de goles anotados.
        """
        self._goles+=no_goles


    def __str__(self) -> str:
        """
        Métod0  mágico que muestra la información de la clase personaje.
        """
        return f"Jugador( Nombre: {self._nombre} |, Número: {self._numero:}|, Goles anotados: {self._goles}|)"

if __name__ == '__main__':
    messi=Jugador("Messi",10,845)
    print(messi)
    messi.anotar_goles(5)
    print(messi)
    messi.anotar_goles(5)
    print(messi)