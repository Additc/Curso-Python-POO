class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre  # Hacemos que forme parte del objeto
        self.temas_aprendidos = []

    def aprender_tema(self,tema:str)->None:
        self.temas_aprendidos.append(tema) # aniadimos un tema a lista de ese objeto
        print(f"{self.nombre} aprendió {tema}")

class Profesor:
    def __init__(self, nombre: str):
        self.nombre = nombre  # Hacemos que forme parte del objeto
        self.temas_dominados =[]

    def dominar_tema(self,tema: str)-> None:
        self.temas_dominados.append(tema)  # aniadimos un tema a lista de ese objeto
        print(f"EL profesor {self.nombre} domina el tema: {tema}")

    def enseniar_tema(self,no_tema:int)->str:
        tema_enseniar=self.temas_dominados[no_tema]
        return tema_enseniar