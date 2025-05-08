"""
Su trabajo es escribir una simple función de validación de contraseñas, como se ve en muchos sitios web.

Las reglas para una contraseña válida son las siguientes:

    Tiene que haber al menos 1 letra mayúscula.
    Tiene que haber al menos una carta minúscula.
    Tiene que haber al menos 1 número.
    La contraseña tiene que ser al menos 8 personajes largos.

Su función toma un argumento de cadena y devuelve si es una contraseña válida, como booleano.
"""




def password(st):
    arregloCaracters = st.split('')
    if st == " ":
        return False
    else:
        if arregloCaracters > 8:
            for i in