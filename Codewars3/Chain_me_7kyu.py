"""
Nombre: Addi Toro Chávez.
Fecha: 27 de mayo del 2025.
Descripción:
Escriba un concatenador de funciones genérico que tome un valor inicial y un array de funciones para ejecutarlo
(array de símbolos en Ruby).
La entrada de cada función es la salida de la función anterior (excepto la primera, que toma el valor inicial como entrada).
Devuelva el valor final una vez completada la ejecución.

"""

def chain(init_val, functions):
    """
    Función que recibe un valor y una función y calcula un valor final.
    """
    for func in functions:
        init_val = func(init_val)
    return init_val

def add10(x): return x + 10
def mul30(x): return x * 30

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(chain(42,[]))
    print(chain(50,[mul30]))
    print(chain(50, [mul30, add10]))

