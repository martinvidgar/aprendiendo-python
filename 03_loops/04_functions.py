###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

import os
os.system('cls')

""" Definición de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la función
    return valor_de_retorno # opcional

"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
    print("Hola!")

saludar()

# Ejemplo de una función con parámetro
def saludar_a(nombre):
    print(f"Hola, {nombre}!")

saludar_a("Martin")

# Funciones con más parámetros
def sumar(a,b):
    suma = a + b
    return suma

resultado = sumar(5, 3)
print(resultado)

# Documentar las funciones con docstring
def restar(a,b):
    """
    Resta dos números y devuelve el resultado
    """
    resta = a - b
    return resta

resultado = restar(5, 3)
print(restar.__doc__)
print(resultado)

# Funciones con valores por defecto
def multiplicar(a, b=2):
    return a * b

print(multiplicar(5))
print(multiplicar(5, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("martin", 25, "perro")
describir_persona("hombre", "martin", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="martin", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21)

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\n")
mostrar_informacion_de(nombre="martin", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora