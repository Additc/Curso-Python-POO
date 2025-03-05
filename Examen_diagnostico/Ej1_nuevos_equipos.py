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



def armar_equipos(algoritmos,hackers,codificadores, ctrl, alumnos):
    alumno1 = random.choice(alumnos)
    alumno2 = random.choice(alumnos)




def menu_p()->None:
    algoritmos=["Hector","Alberto", "Addi"]
    hackers=["Tania","Patricia", "Rebeca"]
    codificadores=["Jamileth","Bryan", "Rosalinda"]
    ctrl=["Galilea","Jennifer", "Juan"]
    alumnos=["Galilea","Jennifer", "Juan","Jamileth","Bryan", "Rosalinda","Tania","Patricia", "Rebeca","Hector","Alberto", "Addi"]
    while True:
        opcion = menu()
        if opcion == 1:
            armar_equipos(algoritmos,hackers,codificadores, ctrl, alumnos )
        elif opcion == 0:
            print("Vuelve pronto.")
            break
        else:
            print("Valor no válido.")

if __name__ == '__main__':
    menu_p()