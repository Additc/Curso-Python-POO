"""
Nombre: Addi Toro Chávez.
Fecha: 11 de abril del 2025
Descripción:
Su tarea es hacer una función que puede tomar cualquier entero no negativo como argumento y devolverlo con sus dígitos en orden descendente. Esencialmente, reorganiza los dígitos para crear el número más alto posible.
Ejemplos:
Entrada: 42145 Producto: 54421
Entrada: 145263 Producto: 654321
Entrada: 123456789 Producto: 987654321
"""
def descending_order(num):
    """
    Función que determina los números primos que existen dentro de un número
    y los suma.
    """
    new = []
    digitos = [int(d) for d in str(num)]  # Se convierte a dígitos
    digitos.sort(reverse=True)            # Ordenamos de mayor a menor

    for i in digitos:
        new.append(i)                    #Se agrega una nueva lista ya con orden descendente

    # Se convierte la lista a números
    return int(''.join(map(str, new)))


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(descending_order(5))
    print(descending_order(10))
    print(descending_order(8))
    print(descending_order(7))
