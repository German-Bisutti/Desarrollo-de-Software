# Trabajo Practico Listas, Vectores y Matrices
# Bisutti German
import math

#1) Realizar una función para normalizar un vector. La función recibe un vector de longitud indeterminada de
#float, y debe devolver un nuevo vector normalizado, es decir el módulo del vector debe ser 1.
#Ejemplo:
"""
vector1 = [1, 1, 1] #-> [0.577…, 0.577…8, 0.577…]
vector2 = [1, 3, 7, 9] # -> [0.084…, 0.253…, 0.591…, 0.760…]

def vectorNormalizado (vector):
    modulo = math.sqrt(sum([x**2 for x in vector]))
    vector_normalizado = [x / modulo for x in vector]
    return vector_normalizado

print(vectorNormalizado(vector1))
print(vectorNormalizado(vector2))
"""
#2) Construir una función que elimine los elementos duplicados en una lista. La función recibe una lista, y
#debe devolver una lista que contenga una sola copia de cada elemento de la lista suministrada.
#Ejemplo:
#lista1 = [1, 4, 1, 5, 4, 1] -> [1, 4, 5]
#lista2 = ["Juan","Luis","Juan","Ana","Luis"] -> ["Juan","Luis","Ana"]
"""
def eliminaDuplicados (lista):
    listaLimpia = []
    for elemento in lista:
         if elemento not in listaLimpia:
            listaLimpia.append(elemento)
    return listaLimpia

lista1 = [1, 4, 1, 5, 4, 1]
lista2 = ["Juan", "Luis", "Juan", "Ana", "Luis"]

print(eliminaDuplicados(lista1))
print(eliminaDuplicados(lista2))
"""
#3) Realizar una función para mostrar por consola un tablero de ta-te-ti. La función recibe una matriz de 3x3
#con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o”, o “ ”(espacio).
#Nota: normalmente evitamos que una función imprima directamente, pero en ocasiones es conveniente.
#Ejemplo:
#tablero = [["x","o"," "],["o"," ","x"],["x"," ","o"]]
#Resultado:
#
#      x | o |
#     ---+---+---
#      o |   | x
#     ---+---+---
#      x |   | o
"""
def tateti (tabla):
    for elemento in range(3):
        print(" "+ tabla[elemento][0] + " | " + tabla[elemento][1] + " | " + tabla[elemento][2])
        if elemento < 2:
            print(" ---+---+---")

tablero = [["x","o"," "],["o"," ","x"],["x"," ","o"]]
tateti(tablero)
"""
#4) Realizar una función para buscar si hay ganador en un juego de ta-te-ti. La función recibe una matriz de
#3x3 con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o” o “ ”(espacio), igual que
#en el ejercicio 3. La función debe devolver un None si no hay ganador, o devolver “x” o “o” según si el
#ganador es la “x” o la “o”.
#Ejemplo:
#tablero1 = [["x","o"," "],["o"," ","x"],["x"," ","o"]] -> None
#tablero2 = [["x","o"," "],["x","o","x"],["x"," ","o"]] -> "x"
"""
def ganador(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]
        
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
        
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    
    return None
    
tablero1 = [["x", "o", " "], ["o", " ", "x"], ["x", " ", "o"]]
tablero2 = [["x", "o", " "], ["x", "o", "x"], ["x", " ", "o"]]

print(ganador(tablero1))  
print(ganador(tablero2)) 
"""
#5) Construir una función para calcular la superficie de un polígono cualquiera, dados sus vértices utilizando la
#fórmula del área de Gauss. La función recibe una lista de vértices, la cantidad de vértices es
#indeterminada. Cada vértice es un vector de dos elementos con la posición (x, y). La función debe devolver
#un float con la superficie del polígono.
#Pueden encontrar el método en:
#https://es.wikipedia.org/wiki/F%C3%B3rmula_del_%C3%A1rea_de_Gauss
#Ejemplo:
#p1 = [[0,0], [0,1], [1,1], [1,0]] -> 1.0
#p2 = [[1,1], [1,4], [5,1]] -> 6.0
"""
def poligono (vertices):
    sumDerecha = 0
    sumIzquierda = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        sumDerecha += x1 * y2
        sumIzquierda += y1 * x2
    
    return abs(sumDerecha - sumIzquierda) / 2

p1 = [[0, 0], [0, 1], [1, 1], [1, 0]]
p2 = [[1, 1], [1, 4], [5, 1]]

print(poligono(p1))
print(poligono(p2))
"""