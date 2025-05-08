"""
Nombre: Addi Toro Chávez.
Fecha: 21 de abril del 2025
Descripción:
Tu compañero escribió un bucle sencillo para listar sus animales favoritos.
Pero parece que hay un pequeño error gramatical que impide que el programa funcione. ¡Corrígelo! :)
Si pasas la lista de tus animales favoritos a la función, deberías obtener la lista de animales con orden y
saltos de línea añadidos.
[ "perro", "gato", "elefante" ]
resultará:
"1. perro\n2. gato\n3. elefante\n"
"""

def list_animals(animals):
    """
    Función que coniverte los animales a una lista con saltos de líneas.
    """
    lst = ""
    for i, animal in enumerate(animals):
        lst += str(i + 1) + '. ' + animal + '\n'
    return lst


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(list_animals([ 'dog', 'cat', 'elephant' ]))
    print(list_animals([ 'bird', 'parrot', 'elephant', 'giraffe' ]))
    print(list_animals([ 'pig', 'frog', 'hamster', 'mouse', 'sloth' ]))