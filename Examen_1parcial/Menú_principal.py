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
    torneo = Torneo("Champions League")
    print(f"Torneo: {torneo._nombre}")
    salir = 1
    while salir != 0:
        print()
        pass
        opciones = menu_principal_torneo()
        if opciones == 1:
            # Pedir lo datos de un jugador y validando cada uno de sus datos
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

            # Creación del jugador
            nuevo_jugador=Jugador(nombre,num)

            # Almacenando en una nueva lista
            nuevos_jugadores.append(nuevo_jugador)
            print("Jugador creado con éxito")
            print()

        elif opciones == 2:
            # Solicitando los datos del equipo y validación de cada uno de ellos
            print("Crear nuevo Equipo de Fútbol")
            nombre_equipo = input("Ingrese nombre del equipo: ")
            while nombre_equipo.isnumeric():
                print("Error")
                nombre_equipo = input("Ingrese nuevamente el nombre del equipo: ")
            nombre_equipo=str(nombre_equipo)

            #Se crea el equipo
            nombre_equipo = Equipo(nombre_equipo)

            #Se almacena en un nueva lista
            nuevos_equipos.append(nombre_equipo)

            print("Equipo creado con éxito")

        elif opciones == 3:
            print()
            # Validación de que existe un jugador
            if len(nuevos_jugadores)>0:
                #Se muestra la lista de jugadores existentes
                print("Lista de Jugadores")
                for i, jugador in enumerate(nuevos_jugadores):
                    print(f"{i + 1}.{jugador}")
                print()
            else:
                print("No hay jugadores")

        elif opciones == 4:
            print()
            # Verificación si hay equipos existentes
            if len(nuevos_equipos)>0:
                #Muestra equipos existentes
                print("Lista de Equipos")
                for i, equipos in enumerate(nuevos_equipos):
                    print(f"{i + 1}.{equipos}|Goles:{equipos.total_goles()}")
                print()
            else:
                print("No hay equipos")

        elif opciones == 5:
            # Verificación de equipos existentes
            if len(nuevos_equipos)==0:
                print("No hay equipos")
            else:
                # Lista de jugadores existentes
                print("Agregar jugador(es) a algún equipo")
                print("Jugadores disponibles:")
                for i, jugador in enumerate(nuevos_jugadores):
                    print(f"{i + 1}.{jugador}")
                print()
                #Lista de equipos existentes
                print("Equipos disponibles")
                for i, equipos in enumerate(nuevos_equipos):
                    print(f"{i + 1}.{equipos}")
                print()

                #Solicitud y validación de índice del equipo a ingresar jugadores
                in_equipo=input("Ingrese el índice del equipo al que desea mover sus jugadores:")
                while not in_equipo.isnumeric():
                    print("Error")
                    in_equipo=input("Ingrese nuevamente el índice del equipo que desea ingresar sus jugadores : ")
                in_equipo=int(in_equipo)-1
                if in_equipo<0 or in_equipo>= len(nuevos_equipos):
                    print("Fuera de rango")
                    break
                else:
                    #Obtener el equipo solicitado
                    equipo=nuevos_equipos[in_equipo]

                    #Validación de jugadores existentes
            if len(nuevos_jugadores)==0:
                print("No hay jugadores para agregar")
            else:
                 # Solicitud y validación de índice de los jugadores a ingresar en un equipo
                print("Selecciona los indices de los jugadores que quiere agregar ejemplo (1,2) ")
                ind_jugador=input("Ingrese los índices:")
                indices=ind_jugador.split(",")


                #Lista para almacenar los jugadores ingresados
                jugadores_a_agregar=[]
                for indice in indices:
                    if indice.isnumeric():
                        #Convertir índice a entero y ajustar el índice
                        numero_jugador=int(indice.strip())-1
                        if numero_jugador>=0 and numero_jugador<len(nuevos_jugadores):
                            jugadores_a_agregar.append(nuevos_jugadores[numero_jugador])
                        else:
                            print("índice no válido")
                        #Accede al equipo y agrega los jugadores con el métod0
                        equipo.agregar_jugadores(*jugadores_a_agregar)
                    else:
                        print("Error índice no válido")

        elif opciones == 6:
            # Verificación de equipos disponibles
            if len(nuevos_equipos) == 0:
                print("No hay equipos disponibles")
            else:
                print("Eliminar jugadores de un equipo")
                print("Equipos disponibles:")
                # Mostrar los equipos disponibles
                for i, equipo in enumerate(nuevos_equipos):
                    print(f"{i + 1}. {equipo._nombre}")

                print()
                # Seleccionar el equipo
                in_equipo = input("Ingrese el índice del equipo al que desea eliminar sus jugadores: ")

                while not in_equipo.isnumeric():
                    print("Error: Ingrese un índice numérico válido.")
                    in_equipo = input("Ingrese nuevamente el índice de equipo: ")

                in_equipo = int(in_equipo) - 1  # Convertir a índice basado en 0
                if in_equipo < 0 or in_equipo >= len(nuevos_equipos):
                    print("Índice fuera de rango.")
                    break
                else:
                    # Seleccionar equipo
                    equipo_seleccionado = nuevos_equipos[in_equipo]
                    print(f"Usted seleccionó al equipo: {equipo_seleccionado._nombre}")
                    print()

                    # Mostrar jugadores del equipo seleccionado
                    print("Seleccione al jugador que desea eliminar:")
                    for i, jugador in enumerate(equipo_seleccionado._jugadores):
                        print(f"{i + 1}. {jugador.nombres}")

                    # Ingresar los índices de los jugadores a eliminar
                    ind = input("Seleccione el índice del jugador (o múltiples índices separados por coma): ")
                    id_jugadores = ind.split(",")  # Permitir múltiples índices

                    #Almacena jugadores a eliminar
                    jugadores_a_eliminar = []
                    for indice in id_jugadores:
                        try:
                            numero_jugador = int(indice.strip()) - 1  # Convertir a índice basado en 0
                            if 0 <= numero_jugador < len(equipo_seleccionado._jugadores):
                                jugadores_a_eliminar.append(equipo_seleccionado._jugadores[numero_jugador])
                            else:
                                print(f"Índice {numero_jugador + 1} no válido.")
                        except ValueError:
                            print("Por favor ingrese un índice numérico válido.")

                    # Eliminar jugadores si se seleccionaron índices válidos
                    if jugadores_a_eliminar:
                        equipo_seleccionado.remover_jugadores(*jugadores_a_eliminar)
                        print("Jugadores eliminados exitosamente.")
                    else:
                        print("No se eliminó ningún jugador del equipo.")


        elif opciones == 7:
            # Verificación de equipos disponibles
            if len(nuevos_equipos) == 0:
                print("No hay equipos disponibles")
            else:
                print("Agregar un equipo al Torneo")
                print("Equipos disponibles:")
                # Mostrar los equipos disponibles
                for i, equipo in enumerate(nuevos_equipos):
                    print(f"{i + 1}. {equipo._nombre}")  # Asegúrate de que 'nombre' esté definido en la clase 'Equipo'
                print()

                if len(nuevos_equipos)==0:
                    print("No hay equipos por agregar")
                else:
                    print("Selecciona los indices de los equipos que quiere agregar ejemplo (1,2): ")
                    ind_equipo = input("Ingrese los índices:")
                    indices = ind_equipo.split(",")

                    equipo_a_agregar = []
                    for indice in indices:
                        numero_equipo = int(indice.strip()) - 1
                        if numero_equipo >= 0 and numero_equipo < len(nuevos_equipos):
                            equipo_a_agregar.append(nuevos_equipos[numero_equipo])
                        else:
                            print("índice no válido")
                    torneo.agregar_equipos(*equipo_a_agregar)

            # Mostrar los equipos en el torneo después de agregar uno
            print(f"Equipos del Torneo {torneo._nombre}:")
            torneo.mostrar_equipos()

        elif opciones == 8:
            if len(nuevos_equipos)==0:
                print("No hay equipos que eliminar")
            else:
                print("Equipos disponibles en el torneo")
                torneo.mostrar_equipos()
                print()
                if len(nuevos_equipos)==0:
                    print("No hay equipos por eliminar")
                else:
                    print("Selecciona los indices de los equipos que quiere eliminar del torneo ejemplo (1,2): ")
                    ind_equipo = input("Ingrese los índices:")
                    indices = ind_equipo.split(",")

                    equipo_a_eliminar = []
                    for indice in indices:
                        numero_equipo = int(indice.strip()) - 1
                        if numero_equipo >= 0 and numero_equipo < len(nuevos_equipos):
                            equipo_a_eliminar.append(nuevos_equipos[numero_equipo])
                        else:
                            print("índice no válido")
                    torneo.remover_equipos(*equipo_a_eliminar)

            # Mostrar los equipos en el torneo después de eliminar
            print("Equipos del Torneo:")
            torneo.mostrar_equipos()


        elif opciones == 9:
            #Validación de que existen jugadores
            if len(nuevos_jugadores)==0:
                print("No existen jugadores")
            else:
                #Mostrar jugadores
                print("Jugadores disponibles:")
                for i, jugador in enumerate(nuevos_jugadores):
                    print(f"{i + 1}.{jugador}")
                print()
                # Seleccionar el jugador
                in_jugador = input("Ingrese el índice del jugador al que desea asignar sus goles: ")
                while not in_jugador.isnumeric():
                    print("Error: Ingrese un índice numérico válido.")
                    in_jugador = input("Ingrese nuevamente el índice de equipo: ")
                in_jugador = int(in_jugador) - 1  # Convertir a índice basado en 0
                if in_jugador < 0 or in_jugador >= len(nuevos_jugadores):
                    print("Índice fuera de rango.")
                else:
                    #Asignación y validación del número de goles
                    goles=input("Ingrese goles anotados: ")
                    while not goles.isnumeric():
                        print("Error: Ingrese un índice numérico válido.")
                        goles = input("Ingrese nuevamente el índice de equipo: ")
                    goles = int(goles)

                    #Incrementar goles al jugador con el métod0 anotar goles
                    nuevos_jugadores[in_jugador].anotar_goles(goles)

        elif opciones == 10:
            # Verificación de equipos disponibles
            if len(nuevos_equipos) == 0:
                print("No hay equipos existentes")
            else:
                print("Seleccione un equipo para ver el total de goles")
                print("Equipos:")
                # Mostrar los equipos disponibles
                torneo.mostrar_equipos()
                print()

                # Seleccionar el equipo
                in_equipo = input("Ingrese el índice del equipo al que desea ver el total de goles: ")

                # Validación de entrada y asegurarse de que sea un número
                while not in_equipo.isnumeric():
                    print("Error: Ingrese un índice numérico válido.")
                    in_equipo = input("Ingrese nuevamente el índice de equipo: ")

                in_equipo = int(in_equipo) - 1  # Convertir a índice basado en 0

                # Validación de rango del índice
                if in_equipo < 0 or in_equipo >= len(nuevos_equipos):
                    print("Índice fuera de rango.")
                else:
                    # Seleccionar el equipo
                    equipo_seleccionado = nuevos_equipos[in_equipo]

                    # Llamar al métod0 total_goles() del equipo seleccionado
                    total_goles_equipo = equipo_seleccionado.total_goles()  # Asumimos que total_goles devuelve el número de goles
                    print(f"El total de goles del equipo {equipo_seleccionado._nombre} es: {total_goles_equipo}")


        elif opciones == 11:
            # Validación para verificar si hay suficientes equipos para generar el rol
            if len(torneo._equipos) < 2:
                print("No hay suficientes equipos en el torneo para generar el rol.")
            else:
                # Llamar al metodo generar_rol
                torneo.generar_rol()


        elif opciones == 0:
            salir = 0
            print("Salió del programa.")
            break
        else:
            print("opcion incorrecta")