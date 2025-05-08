"""
Nombre: Addi Toro Chávez.
Fecha: 18 de abril del 2025
Descripción:
Suma de primos

La suma de los primos menores o iguales a 10 es 2 + 3 + 5 + 7 = 17.
Halla la suma de todos los primos menores o iguales al número introducido.
"""
def summation_of_primes(primes):
    """
    Suma que calcula la suma de los número primos menores o iguales
    al número introducido.
    """
    primes = int(primes)
    primos = []
    for i in range(2, primes+1 ):
        es_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return sum(primos)

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    print(summation_of_primes(5))
    print(summation_of_primes(6))
    print(summation_of_primes(7))
    print(summation_of_primes(8))
    print(summation_of_primes(9))

