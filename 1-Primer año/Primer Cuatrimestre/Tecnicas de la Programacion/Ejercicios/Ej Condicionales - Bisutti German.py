# Ejercicios Condicionales
#1) Corregir el código para cumplir con la consigna. Ingresar la edad. Si es mayor de 16 años, informar la edad
"""
edad=int(input('Ingrese su edad:'))
if (16 < edad):
 print('La edad es:',edad)
"""

#2) Corregir el código para cumplir con la consigna.Ingresar el valor de 2 dados (de 6 caras) indicar si la suma es mayor o menor que 7.
"""
dado1=int(input('Ingrese el valor del 1er dado:'))
dado2=int(input('Ingrese el valor del 2do dado:'))
suma= dado2+dado1
if (suma > 7):
    print('La suma es mayor a 7')
elif (suma < 7):
    print('La suma es menor a 7')
else:
    print('La suma es 7')
"""

#3) Ingresar la edad. Si es menor de 18 años, informar que debe ser mayos de 18 años.
"""
edad=int(input('Ingrese edad:'))
if (edad < 18):
 print('debe ser mayor')
"""

#4) Ingresar la edad. Si es menor de 18 años, informar que debe ser mayos de 18, si es mayor, pedir el nombre y apellido.
"""
edad=int(input('Ingrese edad:'))
if (edad < 18):
 print('debe ser mayor de 18')
else: 
 nombre = input('Ingrese nombre:')
 apellido = input('Ingrese apellido:')
 print(nombre + " " + apellido)
 """

#5) Ingresar la edad. Si es menor de 16, informar que debe ser mayor de 16. Si esta entre 16 y 18, ingresar el nombre y el nombre de un mayor responsable. Si es mayor de 18 ingresar el nombre.
"""
edad=int(input('Ingrese edad:'))
if (edad < 16):
 print('debe ser mayor de 16')
elif (16 <= edad <= 18):
 nombre = input('Ingrese nombre:')
 responsable = input('Ingrese nombre de responsable:')
 print(nombre)
 print(responsable)
else: 
 nombre = input('Ingrese nombre:')
 apellido = input('Ingrese apellido:')
 print(nombre + " " + apellido)
"""

#6) Ingresar el nombre y la edad. Si la edad es mayor de 16, mostrar una bienvenida incluyendo el nombre. Si es menor, informar que debe ser mayor de 16.
"""
edad=int(input('Ingrese edad:'))
nombre = input('Ingrese nombre:')
if (edad > 16):
 print('Bienvenido ', nombre)
else: 
 print('Debe ser mayor a 16')
"""

#7) Ingresar 3 números. Calcular el promedio en una nueva variable. Si el promedio en menor que 4, informar que está desaprobado. Si el promedio es entre 4 y 7 informar que debe rendir final. Si el promedio es igual o mayor a 7 informar que promociona y la nota final.
"""
num1 = int(input("Ingresar numero 1: "))
num2 = int(input("Ingresar numero 2: "))
num3 = int(input("Ingresar numero 3: "))
promedio = (num1 + num2 + num3) / 3
if (promedio < 4):
    print("Esta desaprobado")
elif (4 <= promedio < 7):
    print("Rinde final")
else:
    print("Promociona con una nota de: ", promedio)
"""