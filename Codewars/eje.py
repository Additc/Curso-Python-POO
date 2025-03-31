def replace_exclamation(st):
    cadena=""
    st=st.lower()
    for i in st:
        if i=="a" or i == "e" or i == "i"or i == "o" or i =="u":
            i="!"
            cadena+=i
        else:
            cadena+=i
    return cadena



if __name__ == '__main__':
    print(replace_exclamation("HOLA"))