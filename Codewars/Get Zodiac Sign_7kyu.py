"""
Nombre: Addi Toro Chávez.
Fecha: 28 de marzo del 2025
Descripción:
Su tarea es obtener el signo del zodíaco
utilizando el día y el mes de entrada.
"""

def get_zodiac_sign(dia, mes):
    """
    Función que retorna el signo zodiacal, de acuerdo al mes y al día ingresados.
    """
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Taurus"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gemini"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cancer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Scorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagittarius"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricorn"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquarius"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Pisces"

if __name__ == '__main__':
    print(get_zodiac_sign(10,10))
    print(get_zodiac_sign(1, 5))
    print(get_zodiac_sign(6, 9))
    print(get_zodiac_sign(25, 11))
