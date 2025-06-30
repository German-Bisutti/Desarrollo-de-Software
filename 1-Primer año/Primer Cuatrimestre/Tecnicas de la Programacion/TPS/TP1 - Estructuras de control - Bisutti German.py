# Trabajo Practico Estructuras de Control
# Bisutti German

# 1) Para una aplicación se necesita validar la fecha ingresada por el usuario. El usuario ingresa un entero
# para el día, un entero para el mes y un entero para el año (año completo, 4 dígitos). No hay que validar
# si los datos ingresados son enteros o no, solo si la fecha es válida. Salida: imprimir “Fecha valida” o
# “Fecha invalida”.
"""
dia=int(input('Ingrese el día:'))
mes=int(input('Ingrese el mes:'))
año=int(input('Ingrese el año:'))

if (año <= 2024):
    if (1 <= mes <= 12):
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            bisiesto = True
        else:
            bisiesto = False
        if mes == 2:
            max_dia = 29 if bisiesto else 28
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            max_dia = 30
        else:
            max_dia = 31
        if 1 <= dia <= max_dia:
            print("Fecha valida")
        else:
            print("Fecha invalida")
    else:
        print("Fecha invalida")
else:
    print("Fecha invalida")
"""
# 2) Para un programa se necesita imprimir por pantalla un listado de las fichas de dominó. Se puede
# utilizar el “0” (cero) para representar las fichas sin puntos. Tener en cuenta que, por ejemplo, “4-5” y
# “5-4” son la misma ficha y no puede estar duplicada en el listado.
"""
for i in range(7):
    for a in range(i, 7):
        print(i, "-", a)
"""

# 3) Realizar un programa para calcular el promedio de cada estudiante. El programa debe calcular el
# promedio de una cantidad indeterminada de alumnos, pero cada estudiante tiene 5 notas en total.
"""
total_alumnos = int(input('cantidad de alumnos a ingresar ?: '))
for i in range(1, total_alumnos+1):
    print("Alumno numero ", i)
    promedio = 0
    for n in range (1, 6):
        nota = int(input("nota: "))
        promedio =  promedio + nota
    print("Promedio alumno numero", i, ": ", promedio/5)
"""

# 4) En una fábrica, una balanza automática pesa tandas de galletitas. Para el ejercicio, los valores se
# ingresan por teclado. Las galletitas se acumulan, cuando el peso acumulado es igual o superior al peso
# que debe tener el paquete, se informa por pantalla para cambiar el paquete. El peso del paquete debe
# ser un parámetro en el programa y puede cambiarse en cada ejecución.
"""
pesoLimite = int(input("Ingrese peso de limite del paquete: "))
pesoGalletitas = 0

while (pesoGalletitas < pesoLimite):
    pesoAgregado = int(input("Cuanto peso se agrega ? : "))
    pesoGalletitas = pesoGalletitas + pesoAgregado
print("Se alcanzo o supero el peso limite, debe agregar otro paquete")
"""

# 5) En una fábrica de panificados se tiene un silo para almacenar la harina. La capacidad del silo debe ser
# un parámetro del programa y se puede cambiar en cada ejecución. Un operario le ingresa la cantidad
# de harina requerida para la preparación (ingreso por teclado). El programa debe informar si la
# cantidad de harina del silo es suficiente para realizar la preparación. Si la cantidad es suficiente lo informa
# y actualiza la cantidad harina restante en el silo. Si no es suficiente, lo informa y cancela la
# preparación. 
"""
capacidadCilo = int(input("Ingrese capacidad del cilo: "))
cantidadHarinaCilo = int(input("Ingrese la cantidad de harina en el cilo: "))
harinaRequerida = int(input("Ingrese harina requerida: "))

if(harinaRequerida <= cantidadHarinaCilo):
    cantidadHarinaCilo = cantidadHarinaCilo - harinaRequerida
    print("La cantidad de harina en el cilo es suficiente, preparacion exitosa")
    if(cantidadHarinaCilo <= 0):
        print("El cilo no tiene mas harina")
else:
    print("La cantidad de harina en el cilo no es suficiente, se cancela la preparacion")
"""