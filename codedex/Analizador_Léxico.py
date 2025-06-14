import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMERO',
    'ID',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIVIDIR',
    'LPAREN',
    'RPAREN'
)

# Expresiones regulares simples
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Regla con acción: números
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignorar espacios
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Leer expresión desde archivo
archivo_entrada = "expresion.txt"
with open(archivo_entrada, "r") as f:
    expresion = f.read().strip()

print(f"Analizando la expresión desde archivo: {expresion}\n")

# Ingresar la expresión al lexer
lexer.input(expresion)

# Abrir archivo de salida para guardar tokens
archivo_salida = "tokens.txt"
with open(archivo_salida, "w") as salida:
    for token in lexer:
        linea = f"Tipo: {token.type}, Valor: {token.value}, Posición: {token.lexpos}"
        print(linea)
        salida.write(linea + "\n")


