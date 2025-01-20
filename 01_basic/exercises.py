###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name, city = input("¿Cómo te llamas y de qué ciudad eres?\n").split(", ")
print(f"{name}\n{city}")

print("----------------------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("----------------------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print("Cadena \"1245\" a entero", int("12345"))
print("Entero \"1245\" a float", float(int("12345")))

print("Convertir 3.99 a entero:", int(3.99))
print("Al convertir 3.99 a entero, el entero elimina la parte decimal y se queda con el número entero")

print("----------------------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = "Martin"
edad = 25
altura = 1.85
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print("----------------------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí´

numero_pi = 3.14159
print("Número PI:", numero_pi)
print("Redondeo:", round(numero_pi))
resultado = int(numero_pi/2)
print("División entera:", resultado)