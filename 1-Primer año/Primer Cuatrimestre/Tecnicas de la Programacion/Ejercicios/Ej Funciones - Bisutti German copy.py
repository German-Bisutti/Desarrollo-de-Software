# Ejercicios Funciones
import random
# 1) Corregir el código para cumplir con la consigna Crear una función que dados 2 números, devolver el promedio
"""
def promedio(valor1, valor2):
    promedio = (valor1 + valor2)/2.0
    return promedio
#Programa principal
n1 = float(input('Ingrese el valor 1: '))
n2 = float(input('Ingrese el valor 2: '))
prom = promedio(n1,n2)
print('Promedio: ',prom)
"""

# 2) Corregir el código para cumplir con la consigna. Crear una función que dados las medidas de 3 segmentos, devuelva True si se puede formar un triángulo y False si no se puede formar un triángulo con ellos.
"""
def es_triangulo (A, B, C):
 if C > (A+B):
   return False
 elif B > (A+C):
   return False
 elif A > (B+C):
   return False
 else:
   return True
#Programa principal
L1 = float(input('Ingrese la longitud del 1er lado: '))
L2 = float(input('Ingrese la longitud del 2do lado: '))
L3 = float(input('Ingrese la longitud del 3er lado: '))
if es_triangulo(L1,L2,L3):
 print('Se puede formar un triángulo')
else:
 print('No se puede formar un triángulo')
"""

# 3) Dado un número, devolver True si es par, False si es impar
"""
def parinpar (num):

    if (num % 2) == 0:
        return true
    else:
        false
numero = int(input("Ingrese un numero"))
parinpar(numero)
"""

#4) Dado dos números, devolver el mayor.
"""
def mayor (num1, num2):
    if num1 > num2:
        print("El numero ", num1, "es mayor")
    elif num1 == num2:
        print("El numero ", num1, "es igual a ", num2)
    else:
        print("El numero ", num2, "es mayor")
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
mayor(n1, n2)
"""

#5) Dado 3 números, devolver el menor.
"""
def menor (num1, num2, num3):
    if num1 <= num2:
        if num1 <= num3:
            print("El numero ", num1, "es menor")
        else:
            print("El numero ", num3, "es menor")
    else:
        if num2 <= num3:
            print("El número", num2, "es el menor")
        else:
            print("El número", num3, "es el menor")
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))
menor(n1, n2, n3)
"""

#6) Dado 3 números, devolver el promedio.
"""
def promedio (num1, num2, num3):
    print((num1 + num2 + num3)/3)
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))
promedio(n1, n2, n3)
"""

#7) Dado un número, devolver True si es primo y False si no es primo. --
"""
def primo (num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
numero = int(input("Ingrese un numero: "))
print(primo(numero))
"""

#8) Construir una función que tire los dados. La función recibe un entero que corresponde a la cantidad de dados a tirar. Todos los dados son de 6 caras. La función devuelve la suma de los valores de los dados. Investigar cómo obtener números al azar.
"""
def dados (cantDados):
    suma = 0
    for i in range(1, cantDados + 1):
        numero = random.randint(1, 6)
        suma = suma + numero
    return suma
cantidad= int(input("Ingrese cantidad de dados: "))
resultado = dados(cantidad)
print("la suma de los dadosa es: ", resultado)
"""
