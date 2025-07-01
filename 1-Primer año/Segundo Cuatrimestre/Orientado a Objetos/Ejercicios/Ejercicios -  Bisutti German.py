
import math
#Ejercicios
#1) Realizar la clase Punto, para almacenar las coordenadas (x, y) de un punto. Realizar una función calcule la
# distancia entre 2 puntos en el plano. La función tiene 2 argumentos que son 2 objetos de la clase Punto.

#2) Realizar la clase Caja, la que guarda las dimensiones de una caja (largo, ancho y alto) y los métodos para
# cambiar las medidas de la caja, para calcular y devolver el volumen de la caja. No utilizar los comandos
# input ni print dentro de la clase (capricho del profesor)

#3) Realizar la clase Dado, que simule el comportamiento y las acciones que se puede hacer con un dado, por
# ejemplo para el juego de la oca, ludo o similar. No utilizar los comandos input ni print dentro de la clase
# (capricho del profesor)

#4) Realizar la clase Cubilete, que permita contener varios dados, tirarlos, visualizar el valor de cada dado y
# calcular y devolver la suma de los valores de los dados. No utilizar los comandos input ni print dentro de la
# clase (capricho del profesor).
#-----------------------------------------------------------------------------
#1-
class Punto:

    def __init__(self, puntoX: int, puntoY: int ) -> None:
        print("Se crea a:", Punto)
        self.puntoX = puntoX
        self.puntoY = puntoY

    def distancia (self, punto2: "Punto") -> None:
        return ((punto2.puntoX - self.puntoX) ** 2 + (punto2.puntoY - self.puntoY) ** 2) ** 0.5



p1 = Punto(3, 5)
p2 = Punto(5, 5)
print("(", p1.puntoX,";", p1.puntoY, ")")
print("(", p2.puntoX,";", p2.puntoY, ")")
print("La distancia entre P1 y P2 es:", p1.distancia(p2))
#2-
class Caja:
    def __init__(self, largo, ancho, alto) -> None:
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def cambiar_medidas(self, nuevo_largo, nuevo_ancho, nuevo_alto) -> None:
        self.largo = nuevo_largo
        self.ancho = nuevo_ancho
        self.alto = nuevo_alto

    def calcular_volumen(self)-> int:
        return self.largo * self.ancho * self.alto
#3-
from random import randint

class Dado:
    def __init__(self)-> None:
        self.cara = None

    def lanzar(self) -> int:
        self.cara = randint(1, 6)
        return self.cara

    def mirar(self) -> int:
        return self.cara
#4-
class Cubilete:
    def __init__(self, cantidad_dados):
        self.dados = [Dado() for _ in range(cantidad_dados)]

    def tirar(self):
        for dado in self.dados:
            dado.lanzar()

    def obtener_valores(self):
        return [dado.mirar() for dado in self.dados]

    def suma_valores(self):
        return sum(self.obtener_valores())