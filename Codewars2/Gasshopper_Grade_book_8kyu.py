"""
Nombre: Addi Toro Chávez.
Fecha: 18 de abril del 2025
Descripción:
Complete la función para que encuentre el promedio de las tres calificaciones
que se le pasaron y devuelva el valor de la letra asociada con esa calificación.
"""
def get_grade(s1, s2, s3):
    """
    Función que calcula el promedio de 3 calificaciones.
    """
    promedio = (s1 + s2 + s3) / 3
    if promedio >= 90 and promedio <= 100:
        return "A"
    elif promedio >= 80 and promedio < 90:
        return "B"
    elif promedio >= 70 and promedio < 80:
        return "C"
    elif promedio >= 60 and promedio < 70:
        return "D"
    elif promedio >= 0 and promedio < 60:
        return "F"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(get_grade(95,90,93))
    print(get_grade(100, 85, 96))
    print(get_grade(75, 60, 33))
    print(get_grade(15, 100, 93))


