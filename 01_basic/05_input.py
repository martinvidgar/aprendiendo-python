###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

print("Hola, ¿cómo te llamas?")
nombre = input()

print(f"Encantado de conocerte, {nombre}")
nombre = input("¿Cómo te llamas?\n")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"En dos años tendrás {age + 2} años")

print("Obtener multiples valores a la vez")
country, city = input("¿De qué país y ciudad eres?\n").split()
print(f"Vives en {city}, {country}")