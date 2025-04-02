"""
Nombre: Addi Toro Chávez.
Fecha: 26 de marzo del 2025
Descripción:
Menú principal
"""


from Jugador import Jugador
from Equipo import Equipo
from Torneo import Torneo


def menu_principal_torneo():
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
    print()
    return opcion


""" %%%%%%%%%%%%%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    nuevos_jugadores=[]
    nuevos_equipos=[]
    salir = 1
    while salir != 0:
        print()
        pass
        opciones = menu_principal_torneo()

        if opciones == 1:
            print("Crear nuevo jugador")
            nombre=input("Ingrese nombre del jugador: ")
            while nombre.isnumeric():
                print("Error")
                nombre=input("Ingrese nuevamente el nombre del jugador: ")
            nombre=str(nombre)
            num=input("Ingrese número del jugador: ")
            while not num.isnumeric():
                print("Error")
                num=input("Ingrese nuevamente el número del jugador: ")
            num=int(num)
            nuevo_jugador=Jugador(nombre,num)
            nuevos_jugadores.append(nuevo_jugador)
            print("Jugador creado con éxito")
            print()

        elif opciones == 2:
            print("Crear nuevo Equipo de Fútbol")
            nombre_equipo = input("Ingrese nombre del equipo: ")
            while nombre_equipo.isnumeric():
                print("Error")
                nombre_equipo = input("Ingrese nuevamente el nombre del equipo: ")
            nombre_equipo = Equipo(nombre_equipo)
            nuevos_equipos.append(nombre_equipo)

            print("Equipo creado con éxito")

        elif opciones == 3:

            print()
            print("Lista de Jugadores")
            for i, jugador in enumerate(nuevos_jugadores):
                print(f"{i + 1}.{jugador}")
            print()

        elif opciones == 4:
            print()
            if len(nuevos_equipos)>0:
                print("Lista de Equipos")
                for i, equipos in enumerate(nuevos_equipos):
                    print(f"{i + 1}.{equipos}|Goles:{equipos.total_goles()}")
                print()
            else:
                print("No hay equipos")

        elif opciones == 5:
            print("Agregar un jugadores a algún equipos")
            print()
            print("Jugadores disponibles:")
            for i, jugador in enumerate(nuevos_jugadores):
                print(f"{i + 1}.{jugador}")
            print()
            print("Equipos disponibles")
            for i, equipos in enumerate(nuevos_equipos):
                print(f"{i + 1}.{equipos}")
            print()
            indice=input("Ingrese el índice del jugador que desea:")

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