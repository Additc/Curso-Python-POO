class Persona: # La definición de la clase siempre va en mayúscula
    #Metodo contructor
    def __init__(self,nombre:str,edad:int,altura:float,peso:float): # Hace referencia a uno mismo y haciendo referencial al objeto utilizado.
        #Atributos de la persona
        self.nombre=nombre  # Hacemos que forme parte del objeto
        self.edad=edad
        self.altura=altura
        self.peso=peso
    #Metodos
    def caminar(self)->None:
        print("Estoy caminando")

    def comer(self)->None:
        print("Estoy comiendo")

    def jugar(self)->None:
        print("Estoy jugando")

    def dormir(self)->None:
        print("Estoy durmiendo")

if __name__=="__main__":
    addi=Persona("Addi Chávez",19,1.70,70) #creamos a las persona

    #Impimimos sus características y accedemos a los atributos de ese objeto
    print(addi.nombre)
    print(addi.edad)
    print(addi.altura)
    print(addi.peso)

    # accedemos a sus métodos
    addi.caminar()