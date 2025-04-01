"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Menú principal
"""


from Jugador import Jugador
from Equipo import Equipo
from Torneo import Torneo


def menu_principal_juegos():
    """
    Muestra el menú de opciones del programa
    :return: La función devuleve la selección del usuario,dentro del menú de opciones
    """
    print("Opciones de juego: ")
    print("1) Crear un nuevo jugador")
    print("2) Crear un nuevo equipo")
    print("3) Ver lista de jugadores")
    print("4) Ver lista de equipos")
    print("5) Agregar jugadores a algún equipo")
    print("6) Eliminar jugadores de un equipo")
    print("7) Agregar equipos al torneo")
    print("8) Eliminar equipos del torneo")
    print("9) Anotar gol(es) a un jugador")
    print("10) Conocer el número total de goles de los equipos ")
    print("11) Generar el rol de juegos")
    print("0) Salir")
    opcion = (input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion = input("Ingrese número nuevamente: ")
    opcion = int(opcion)
    return opcion

if __name__ == '__main__':
    salir = 1
    while salir != 0:
        print()
        pass
        opciones = menu_principal_juegos()
        if opciones == 1:
            pass
        elif opciones == 2:
            pass
        elif opciones == 3:
            pass
        elif opciones == 4:
            pass
        elif opciones == 5:
            pass
        elif opciones == 6:
            pass
        elif opciones == 7:
            pass
        elif opciones == 8:
            pass
        elif opciones == 9:
            pass
        elif opciones == 10:
            pass
        elif opciones == 11:
            pass
        elif opciones == 0:
            salir = 0
            print("Salió del programa.")
            break
        else:
            print("opcion incorrecta")