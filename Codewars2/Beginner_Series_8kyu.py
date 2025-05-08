"""
Nombre: Addi Toro Chávez.
Fecha: 19 de abril del 2025
Descripción:
Tus compañeros te pidieron que les copiaras un trabajo.
Sabes que hay 'n' compañeros y que el trabajo tiene 'm' páginas.
Tu tarea es calcular cuántas páginas en blanco necesitas.
Si n < 0 o m < 0, devuelve 0.
"""

def paperwork(n, m):
    """
    Función que calcula las páginas en blanco que se necesitan.
    """
    if n>0 and m>0:
        pag=n*m
        return pag
    else:
        return 0


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(paperwork(5,5))
    print(paperwork(-5,5))
    print(paperwork( 2,7))
    print(paperwork(4,6))