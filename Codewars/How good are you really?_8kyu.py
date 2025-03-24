"""
Nombre: Addi Toro Chávez.
Fecha: 20 de marzo del 2025
Descripción:
Hubo un examen en tu clase y lo aprobaste. ¡Felicidades!
Pero eres ambicioso. Quieres saber si eres mejor que el promedio de tu clase.
Recibirás una matriz con las puntuaciones de tus compañeros. ¡Ahora calcula el promedio y compáralo!
Devuelve "true" si eres mejor; de lo contrario, "false".
Nota:
Tus puntos no se incluyen en la matriz de puntos de tu clase. ¡No los olvides al calcular el promedio!
"""

def better_than_average(class_points, your_points):
    """
    Función que calcula el promedio de puntos y compara si es menor o mayor al puntaje personal.
    :param class_points: Lista de número de puntos de una clase.
    :param your_points: Puntaje personal.
    :return: True en caso de que el puntaje personal es mayor al de la clase o en caso contrario false.
    """
    total=0
    for i in class_points:
        total+=i
    promedio=total/len(class_points)
    if promedio<your_points:
        return True
    else:
        return False

if __name__ == '__main__':
    print(better_than_average([2,3],5))
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88],75))
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90],69))
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33],50))
    print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28],21))
    print(better_than_average([100, 90, 80],85))