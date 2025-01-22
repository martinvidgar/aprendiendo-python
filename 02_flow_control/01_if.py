###
# 01 - Sentencias condiciones (if, else, elif)
# Permiten ejecutar un bloque de código si se cumple una condición
###

import os
os.system('cls') # NOTA: Funciona en terminal linux o mac. En windows usar 'cls'

print("\nSentencia condicional con if");

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

print("\nSentencia condicional con else");
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia condicional con elif");
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

print("\nCondiciones multiples");
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir 🚗")
else:
    print("POLICIA 🚔 - No puede conducir")

if edad >= 18 or tiene_carnet:
    print("Puede conducir 🚗")

es_fin_de_semana = False
# Javascript --> !
if not es_fin_de_semana:
    print("Es un día laboral")

print("\nAnidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puede ir de fiesta")
    else:
        print("Quedate en casa")
else:
    print("No puedes ir de fiesta")


numero = 5
if numero: # True
    print("El número es cinco")

numero = 0
if numero: # False
    print("El número es cero")

numero = ""
if numero:
    print("La cadena no está vacía")

numero = 5
if numero == 3:
    print("El número es 3")

numero = 3
es_el_tres = numero == 3
if es_el_tres:
    print("El número es 3")


print("\nLa condicion ternaria")
# es una forma concisa de un if else en una linea de codigo
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)