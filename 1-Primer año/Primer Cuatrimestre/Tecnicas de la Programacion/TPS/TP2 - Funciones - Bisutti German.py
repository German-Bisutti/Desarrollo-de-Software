# Trabajo Practico Funciones
# Bisutti German
import math

# 1) Construir una función calcule la distancia entre 2 puntos en el plano. La función tiene 4 argumentos (x1,
# y1, x2, y2) que son las coordenadas de los puntos. Los tipos de datos de entrada y salida son punto
# flotante (float). Opcional, la función recibe 2 vectores (de 2 elementos) en lugar de 4 valores
"""
def distancia (x1: float, y1: float, x2: float, y2: float) -> float:
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

print (distancia(1, 20, 20, 20))
"""
"""
def distancia (punto1: list[float], punto2: list[float]) -> float:
    dist = math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)
    return dist

print (distancia([10, 20], [20, 20]))
"""
# 2) Realizar una función que, dadas las 3 dimensiones en centímetros de una caja, devuelva el volumen total
# en litros. Realizar otra función que, dadas las 3 dimensiones en centímetros de una caja, devuelva la
# superficie total de la caja en cm². Entrada: las 3 dimensiones en centímetros. Salida: el volumen (en litros)
# y la superficie total (en cm²). Opcional, Realizar una sola función que reciba las dimensiones de la caja y
# devuelva tanto el volumen, como la superficie de la caja, simultáneamente.
"""
def Caja (a: float, b: float, c: float) -> float:
    totalLitros = (a * b * c)/1000
    totalSuperficie = (2*(a*b + a*c + b*c))
    return totalLitros, totalSuperficie 
print("Litros de la caja:", Caja(10, 10, 10)[0], "\nSuperficie total en cm² ", Caja(10, 10, 10)[1])
"""
# 3) El método más fácil para encriptar un mensaje consiste en el de desplazamiento, cada carácter se desplaza
# una cantidad fija llamada clave. Por ejemplo si la clave es 1, la palabra HOLA sería IPMB. Realizar 2
# funciones, una para encriptar y otra para desencriptar. A la función se le pasa el texto y la clave (un
# entero), y debe devolver un texto. Una pista, la función ord() convierte un carácter en un su código ASCII y
# la función chr() convierte el código ASCII en carácter. Tener en cuenta que el texto resultante debe estar
# compuesto por las letras del abecedario. Pueden ignorar las diferencias entre mayúsculas y minúsculas, y
# pueden ignorar de convertir los signos de puntuación. Opcional, pueden hacer el encriptado más
# complejo. Opcional, pueden hacer una sola función que encripte y desencripte, a la misma se le pasa el
# texto, la clave (igual que entes) y la operación que se desea realizar (encriptar o desencriptar).
"""
def encriptar (clave: int, texto:str) -> str:
    encriptado = ""
    for i in texto:
        caracter = ord(i)
        codigo = caracter + clave
        encriptado += chr(codigo)
    return encriptado
print(encriptar(1, "HOLA"))

def desencriptar (clave: int, texto:str) -> str:
    desencriptado = ""
    for i in texto:
        caracter = ord(i)
        codigo = caracter - clave
        desencriptado += chr(codigo)
    return desencriptado
print(desencriptar(1, "IPMB"))

def encriptamiento (clave: int, texto:str, funcion:str):
    if(funcion == "encriptar"):
        return encriptar(clave, texto)
    elif(funcion == "desencriptar"):
        return desencriptar(clave, texto)
    else:
        return ("No a seleccionado funcion")

print(encriptamiento (1, "HOLA", "encriptar"))
print(encriptamiento (1, "IPMB", "desencriptar"))
"""
# 4) Construir una función que reciba el primer nombre, el segundo nombre y apellido de una persona y
# devuelva un string con Apellido, Primer nombre inicial del segundo nombre punto. Tener en cuenta que el
# segundo nombre es opcional en ese caso no devuelve la inicial del segundo nombre. Opcional, convertir a
# mayúscula la inicial de cada nombre y apellido
"""
def denominacion (nombre1: str, apellido: str, nombre2: str = "") -> str:
    if (nombre2):
        return  apellido.capitalize() + " " + nombre1[0].upper() + "." + nombre2[0].upper() + "."
    else:
        return  apellido.capitalize() + " " + nombre1[0].upper() + "."
    
print(denominacion("german", "bisutti"))
"""
# 5) Realizar una función para calcular la cantidad de rollos de empapelado que se necesita para empapelar
# una habitación. La función recibe las dimensiones de la habitación en metros (largo, ancho y alto), el ancho
# del rollo en cm y el largo del rollo en metros, debe devolver un entero con la cantidad de rollos requerida.
# Tengan en cuenta que, la habitación es rectangular y la altura es pareja en toda ella. Al empapelar las tiras
# se colocan verticalmente, cada tira debe entrar entera en toda la altura de la pared (si lo que sobra en el
# rollo es menos que la altura de la habitación, se debe desechar), se puede hacer que una tira cubra una
# esquina (la tira se comparte por 2 paredes). Nota: no tener en cuenta las aberturas como ventanas o
# puertas. Opcional, si no se especifican las dimensiones el rollo se debe calcular con rollos de 52cm de
# ancho y 10 m de largo
"""
def empapelado (largo:float, ancho:float, alto:float, anchoRollo:float = 52, largoRollo:float = 10) -> int:
    anchoRolloM = anchoRollo / 100
    perimetro = 2 * (largo + ancho)
    cantidadTiras = math.ceil(perimetro / anchoRolloM)
    tiras = math.floor(largoRollo / alto)
    totalRoyos = math.ceil(cantidadTiras / tiras)
    return totalRoyos

print(empapelado(5, 10, 3, 52, 10))
"""