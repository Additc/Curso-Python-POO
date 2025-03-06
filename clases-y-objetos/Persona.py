class Persona: # La definición de la clase siempre va en mayúscula
    #Metodo contructor
    def __init__(self,nombre:str,edad:int,altura:float,peso:float): # Hace referencia a uno mismo y haciendo referencial al objeto utilizado.
        #Atributos de la persona
        self.nombre=nombre  # Hacemos que forme parte del objeto
        self.edad=edad
        self.altura=altura
        self.peso=peso
    #Métodos
    def caminar(self)->None:
        print(f"{self.nombre} esta caminando para bajar sus {self.peso} kgs.")

    def comer(self)->None:
        print(f"{self.nombre} esta comiendo para aumentar su estatura de {self.altura} cm.")

    def jugar(self)->None:
        print(f"{self.nombre} esta jugando con sus amigos Call of duty.")

    def dormir(self)->None:
        print(f"{self.nombre} esta durmiendo")

if __name__=="__main__":
    addi=Persona("Addi",19,1.70,70) #creamos a las persona

    #Impimimos sus características y accedemos a los atributos de ese objeto
    print(f"nombre:{addi.nombre}")
    print(f"edad:{addi.edad}")
    print(f"altura:{addi.altura}")
    print(f"peso:{addi.peso}")

    # accedemos a sus métodos
    addi.caminar()
    addi.comer()
    addi.jugar()
    addi.dormir()

    print()
    #SEGUNDO OBJETO
    compa=Persona("Alberto",20,1.68,65) # Se utiliza la clase como una plantilla
    compa.caminar()
    compa.comer()
    compa.jugar()
    compa.dormir()
    print()

    #modificando edad y peso
    addi.peso=68.5
    addi.edad=20
    addi.caminar()
    print(addi.nombre) # se imprime el nombre
    print(f"edad:{addi.edad}")
    print(f"peso:{addi.peso}")