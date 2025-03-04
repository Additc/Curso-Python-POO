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

algortimos=["Hector","Alberto", "Addi"]
hackers=["Tania","Patricia", "Rebeca"]
codificadores=["Jamileth","Bryan", "Rosalinda"]
ctrl=["Galilea","Jennifer", "Juan"]
alumnos=["Galilea","Jennifer", "Juan","Jamileth","Bryan", "Rosalinda","Tania","Patricia", "Rebeca","Hector","Alberto", "Addi"]

equipo1=[]
equipo2=[]
equipo3=[]
equipo4=[]
equipo5=[]
equipo6=[]

contador=1

for i in range (0,6):
    alumno1= random.choice(alumnos)
    alumno2= random.choice(alumnos)
    print(f"El equipo {contador} es {alumno1,alumno2}")
    contador+=1
