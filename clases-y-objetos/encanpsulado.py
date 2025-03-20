"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Relación de clases
"""

class Cuentabancaria:
    def __init__(self,titular:str,saldo_inicial:float=0): #el 0 aquí hace que no sea necesario mandar el saldo
        self.titular=titular
        self._saldo=saldo_inicial

    def depositar (self,cantidad:float)->None:
        self._saldo+=cantidad

    def retirar(self,cantidad:float)->None:
        self._saldo-=cantidad

    #Metodo de acceso get
    @property
    def saldo(self)->float:
        return self._saldo

    #Metodo de acceso set
    @saldo.setter
    def saldo(self,nuevo_saldo:float)->None:
        self._saldo=nuevo_saldo

    def __str__(self) -> str:
        return f"Cuenta Bancaria( Sueldo:{self._saldo})"

if __name__ == '__main__':
    cuenta_guadalupe=Cuentabancaria("Guadalupe")
    cuenta_guadalupe.saldo=5

"""
CuentaBancaria
-titular:str        Privado
#_saldo:float       Bloqueo
-------------------
+ __init__(titula:str,saldo_incial:float=0)    Publico
+ depositar(cantidad:float)None                Publico
+ retirar(cantidad:float):None                 Publico
+ __str__():str                                Publico

"""