'''
Nombre: Addi Toro Chavez
Fecha: 4 de marzo de 2025.
Descripción: Evalucación diagnostica.

El curso tiene los siguientes equipos:

    Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
    Los Hackers de Café: Tania, Patricia, Rebeca.
    Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
    Los Ctrl+Z: Galilea, Jennifer, Juan.


Este programa debe generar 6 nuevos equipos de 2 personas cada uno,
pero con la restricción de que no puede haber dos personas que ya estuvieron en el mismo equipo de arriba ☝️.
'''

from random import choice
import random

def menu():
    """
    Función donde se encuentra el menú de opciones
    :return: La opción seleccionada por el usuario.
    """
    print()
    print("Menú de opciones")
    print("1) Generar equipos")
    print("2) salir")
    opcion=input("Ingrese una opción a realizar: ")
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Intenta nuevamente: ")
    opcion = int(opcion)
    print()
    return opcion



def armar_equipos(alumnos):
    for i in range(0,6):
        alumno1 = random.choice(list(alumnos.keys()))
        alumno2 = random.choice(list(alumnos.keys()))
        while alumnos.get(alumno1) == alumnos.get(alumno2):
            alumno1 = random.choice(list(alumnos.keys()))
            alumno2 = random.choice(list(alumnos.keys()))
        print(f"El equipo {i+1}: {alumno1} y {alumno2}")
        alumnos.pop(alumno1)
        alumnos.pop(alumno2)




def menu_p()->None:
    alumnos={"Hector":1,"Alberto":1, "Addi":1,
            "Tania":2,"Patricia":2, "Rebeca":2,
            "Jamileth":3,"Bryan":3, "Rosalinda":3,
            "Galilea":4,"Jennifer":4, "Juan":4}
    while True:
        opcion = menu()
        if opcion == 1:
            armar_equipos(alumnos)
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Valor no válido.")

if __name__ == '__main__':
    menu_p()