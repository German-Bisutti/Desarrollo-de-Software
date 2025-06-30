# Ejercicios Vectores
#1) Corregir el código para cumplir con la consigna.
#Ingresar 5 números y guardarlos en un vector. Al finalizar informar el número menor.
"""
vector = []
for n in range(5):
 nuevo = float(input("Ingrese el siguiente número:"))
 vector.append(nuevo)

menor = vector[0]
5
for elemento in vector:
 if elemento < menor:
   menor = elemento

print ("El número menor es:", menor)
"""

#2) Dado el siguiente vector [1, 5, 3, 9, 10, 8], informar el número mayor.
"""
vector = [1, 5, 3, 9, 10, 8]
mayor = vector[0]
for elemento in vector:
    if  mayor < elemento:
        mayor = elemento
print ("El número mayor es:", mayor)
"""

#3) Dado el siguiente vector [5, 9, 15, 2, -8, 3], informar el número mayor y el número menor.
"""
vector = [5, 9, 15, 2, -8, 3]
mayor = vector[0]
menor = vector[0]

for elemento in vector:
    if  mayor < elemento:
        mayor = elemento
    if elemento < menor:
        menor = elemento

print ("El número mayor es:", mayor, "y el numero menor es:", menor)
"""

#4) Dado el siguiente vector [-5, -9, -15, -2, -8, -3], informar el número mayor y el número menor.
"""
vector = [-5, -9, -15, -2, -8, -3]
mayor = vector[0]
menor = vector[0]

for elemento in vector:
    if  mayor < elemento:
        mayor = elemento
    if elemento < menor:
        menor = elemento

print ("El número mayor es:", mayor, "y el numero menor es:", menor)
"""

#5) Dado el siguiente vector [8, 10, 15, 2, 8, 6, 21, 5], informar los dos números mayores.
"""
vector = [-5, -9, -15, -2, -8, -3]
mayor1 = vector[0]
mayor2 = vector[0]

for elemento in vector:
    if  mayor2 < mayor1 < elemento:
        mayor1 = elemento
    else:
        mayor2 = elemento
print ("Los números mayores son:", mayor1, mayor2)
"""

#6) Dado el siguiente vector [5,-2, 8, 10, -4, 13, 21], a cada elemento, sumarle 2, y guardarlo en un
#nuevo vector.
"""
vector = [5,-2, 8, 10, -4, 13, 21]
vector2 = [0]
for elemento in vector:
    vector2.append(elemento =+ 1)

print ("Los números mayores son:", vector2 )
"""

#7) Ingresar 10 números y guardarlos en un vector nuevo. Al finalizar informar el número mayor y el
#número menor.
"""
vector = []
for n in range(10):
 nuevo = float(input("Ingrese el siguiente número:"))
 vector.append(nuevo)

menor = vector[0]
mayor = vector[0]

for elemento in vector:
    if  mayor < elemento:
        mayor = elemento
    if elemento < menor:
        menor = elemento

print ("El número mayor es:", mayor, "y el numero menor es:", menor)
"""

#8) Ingresar 10 números y guardarlos en un vector nuevo. Al finalizar informar el promedio.
"""
vector = []
for n in range(10):
 nuevo = float(input("Ingrese el siguiente número:"))
 vector.append(nuevo)

suma = 0

for elemento in vector:
 suma += elemento

promedio = suma / 10
print ("El promedio es:", promedio)
"""

#9) Ingresar números hasta que se ingrese un 0 (cero). Guardar los números ingresados en un vector,
#ignorar el 0 (cero). Al finalizar informar el número mayor, el número menor y el promedio.
"""
vector = []
numero = float(input("Ingrese un número: "))

while numero != 0:
    vector.append(numero)
    numero = float(input("Ingrese un número: "))

menor = vector[0]
mayor = vector[0]
suma = 0

for elemento in vector:
        suma += elemento
        if mayor < elemento:
            mayor = elemento
        if elemento < menor: 
            menor = elemento

promedio = suma / len(vector)
print ("El promedio es:", promedio, "\nEL numero mayor es:", mayor, "\nEl numero menor es:", menor)
"""
#10) Ingresar números hasta que se ingresa un número negativo. Guardar los números en un vector,
#ignorar el último número negativo. Al finalizar informar la diferencia entre el primer elemento y el
#segundo, entre el segundo elemento y el tercero… hasta informar la diferencia entre el anteúltimo
#elemento y el último.
"""
vector = []
numero = float(input("Ingrese un número: "))

while numero >= 0:
    vector.append(numero)
    numero = float(input("Ingrese un número: "))

for elemento in range(len(vector) - 1):
    if vector[elemento] < vector[elemento + 1]:
        diferencia = vector[elemento + 1] - vector[elemento]
    else:
        diferencia = vector[elemento] - vector[elemento + 1]


    print("La diferencia entre el elemento", (elemento + 1), "y el elemento", (elemento + 2), "es:", diferencia)
"""