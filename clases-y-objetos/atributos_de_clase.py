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

if __name__=="__main__":
    #Creamos 2 empleados
    empleado1=Empleado("Addi",500)
    empleado2=Empleado("Alberto",250)

    print(empleado1)