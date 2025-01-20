##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asignar una variable
# solo hace falta poner esto
my_name = "Martin"
print(my_name)

age = 25
print(age)

# age = 39
# print(age)

# Tipado dinámico: el tipo de dato se determine en tiempo de ejecución
# que no tienes que declararlo explícitamente
name = "Martin"
print(type(name))

name = 25
print(type(name))

# Tipado fuerte: Python no realiza conversione de tipo automáticas
# print(10 + "2")

# f-string (literal de cadena de formato)
# desde la versión Python 3.6
print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
name, age, city = "Martin", 25, "España"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

miNombreDeVariable = "no-recomendado" # camelCase
MiNombreDeVariable = "no-recomendado" # PascalCase
minombredevariable = "no-recomendado" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# nombres no válidos de variables
# 123123_variable = "ko" 
# mi-variable = "ko"
# mi variable = "ko"


# PALABRAS RESERVADAS
# True = False

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True
print(is_user_logged_in)

name: str = "Martin"
print(name)