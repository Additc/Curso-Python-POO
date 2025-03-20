"""
Nombre: Addi Toro Chávez.
Fecha: 17 de marzo del 2025
Descripción:
Relación de clases
"""

class Empleado:
    #Una variable de clase/ o variable de global siempre va en esta parte
    no_id=1
    def __init__(self,nombre:str,sueldo:float):
        self.nombre=nombre
        self.sueldo=sueldo
        self.id=Empleado.no_id #Le asignamos un número e incrementamos
        Empleado.no_id +=1

    def aumentar_sueldo(self,porcentaje:float)->None:
        pass

    def __str__(self) -> str:
        return f"Empleado(id={self.id} nombre:{self.nombre} Sueldo: {self.sueldo})"


class Empresa:
    def __init__(self,nombre:str,*empleados:Empleado):
        self.nombre=nombre
        self.empleados = list(empleados)

    def agregar_empleados(self,*nuevos_empleados:Empleado):
        """
        Se utiliza para agregar más empleados (*vargs) a la empresa.
        :param nuevos_empleados: Los empleados (*vargs) que se agregan a la empresa.
        :return:
        """
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def remover_empleados(self, *empleados_a_remover: Empleado) -> None:
        """
        Se utiliza para remover un empleado de la empresa.
        :param empleados_a_remover: Empleado a remover de la empresa.
        """
        for empleado in empleados_a_remover: #Aquí emplado a remover es una tupla.
            if empleado in self.empleados: #Si el empleado esta dentro de la lista, remueve el empleado.
                self.empleados.remove(empleado)

            else:
                print(f"El empleado {empleado} no forma parte de {self.nombre}.")

    def aumentar_sueldo_empleados(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo a todos los empleados de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        for empleado in self.empleados:
            empleado.aumentar_sueldo(porcentaje=porcentaje)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        #list compression
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"




if __name__ == '__main__':
    addi=Empleado("Addi",250)
    alberto=Empleado("Alberto",250)
    print(addi)
    print(alberto)
    print()

    #Crear clase empresa, dandole un nombre y empleados
    unsij=Empresa("unsij",addi)

    #Agregar métodos a otra clase
    unsij.agregar_empleados(addi,alberto)
    print(unsij)
    print()

    addi.nombre = "paps"
    print(addi)
    print(addi.nombre)