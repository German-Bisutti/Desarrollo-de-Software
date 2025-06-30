# Ejercicios Ciclos
# 1) Corregir el código para cumplir con la consigna. Imprimir la tabla de multiplicar del 4 del 0 al 10.
"""
for i in range (11):
 multiplicacion = i * 4
 print(i, '* 4 =', multiplicacion)
"""

# 2) Corregir el código para cumplir con la consigna. Ingresar números hasta que la suma sea mayor a 10. Al finalizar imprimir el resultado de la suma.
"""
suma=0
while suma<10:
 nuevo = int(input ('Ingrese un nuevo número:'))
 suma = suma + nuevo
print ('La suma es: ', suma)
"""

# 3) Mostrar los números del 1 al 10. Un número por línea.
"""
num=1
while num <= 10:
    print("numero:", num)
    num = num + 1
"""

# 4) Mostrar los números del 10 al 1. Un número por línea.
"""
num=10
while 0 < num:
    print("numero:", num)
    num = num - 1
"""

# 5) Mostrar los números del 1 al 12, en dos columnas. La primera columna con los números impares, la segunda con los números pares.
"""
for num in range(1, 13, 2):
            print(num, num + 1)
"""

# 6) Mostrar los números del 1 al 12, en dos columnas. La primera columna con los número del 1 al 6, la segunda con los números del 7 al 12.
"""
for num in range(1, 7):
    col2 = num + 6
    print(num, col2)
"""

# 7) Ingresar números y sumarlos en una variable nueva, hasta que se ingresa un 0 (cero)
"""
numeros = int(input("Ingrese numero: "))
while (numeros != 0):
    numeros = int(input("Ingrese otro numero: "))
print("Ingreso el numero 0")
"""

# 8) Ingresar números y sumarlos en una variable nueva, hasta que se ingresa un 0 (cero). Al finalizar la carga, informar el promedio (descartando el último 0).
"""
numeros = float(input("Ingrese numero: "))
bucles = 0
promedio = 0
while (numeros!= 0):
    bucles = bucles + 1
    promedio = numeros + promedio
    numeros = float(input("Ingrese otro numero: "))
promedio = promedio / bucles
print("Promedio: ", promedio)
"""

# 9) Ingresar números y sumarlos hasta que la suma sea igual o mayor a 20. Al finalizar informar el promedio.
"""
bucle = 1
numeros = float(input("Ingrese numero: "))
suma = numeros
while (suma < 20):
    bucle = bucle + 1
    numeros = float(input("Ingrese numero: "))
    suma = suma + numeros
print("La suma es igual o mayor a 20, su promedio es: ", suma/bucle)
"""
