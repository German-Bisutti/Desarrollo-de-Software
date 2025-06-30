#
# TP 1 Objetos
# 1) Realizar un programa para calcular el monto total a pagar por cada mesa en un restaurante. Realizar el
#programa usando objetos para almacenar la información de los pedidos de cada mesa y calcular el importe
#total a pagar. ¿Qué estructura de datos necesita para almacenar la información?

#2) Realizar un programa que ayude al pintor a realizar el presupuesto. El programa debe calcular la superficie
#total a pintar y la cantidad de litros de pintura, de una cantidad indeterminada de habitaciones. Cada
#pared puede tener una abertura (puertas, ventanas, etc.), o no tener ninguna abertura. Las aberturas no
#se pintan, restar su superficie de las paredes a pintar.
#¿Qué estructura de datos necesita para almacenar la información?
#Realizar el programa usando objetos para almacenar la información de las habitaciones. Está prohibido el
#uso de las instrucciones print() e input() dentro de las clases (capricho del profesor).

#3) Realizar el programa usando objetos. Está prohibido el uso de las instrucciones print() e input() dentro de
#las clases (capricho del profesor).
#El programa debe permitir:

#A) Cargar países, almacenando el nombre, el nombre de su capital y su población.

#B) Cargar los países limítrofes a un país ya cargado. Los países limítrofes deben ser objetos ya creados en el
#punto A. Cuando al país A, se le carga el país limítrofe B, automáticamente se cargue en el país B, el país
#limítrofe A. Es decir, si a Argentina le cargamos el país limítrofe Uruguay, automáticamente se debe cargar
#a Uruguay el país limítrofe Argentina.

#D) El usuario selecciona un país, y el programa muestra todos sus países limítrofes.
#¿Qué estructura de datos necesita para almacenar la información? ¿Cuántas clases son necesarias? ¿Cómo
#codificar la información?

#1)
"""
class Pedido:
    def __init__(self, numero:int, cantidad:int, precio:float):
        self.numero = numero
        self.precio = precio
        self.cantidad = cantidad

class Mesa: 

    def __init__(self, pedidos: list[Pedido]):
        print("Se crea :", Mesa)
        self.pedidos = pedidos

    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            subtotal = pedido.cantidad * pedido.precio
            print(f"Pedido {pedido.numero}: {pedido.cantidad} x ${pedido.precio} = {subtotal}")
        
    def calcular_total(self) -> float:
        total = 0
        for pedido in self.pedidos:
            total += pedido.cantidad * pedido.precio
        return total
    
    def vaciar_mesa(self):
        self.pedidos = []

    def agregar_pedido(self, cantidad: int, precio: float):
        nuevo_numero = len(self.pedidos) + 1
        nuevo_pedido = Pedido(nuevo_numero, cantidad, precio)
        self.pedidos.append(nuevo_pedido)

if __name__ == "__main__":
    cantidad_pedidos = int(input("Ingrese cantidad de pedidos: "))
    pedidos = []
    for i in range(cantidad_pedidos):
        print(f"--- Pedido {i + 1} ---")
        pedido_cantidad = int(input("Cantidad: "))
        pedido_precio = int(input("Precio: "))
        pedidos.append(Pedido(i + 1, pedido_cantidad, pedido_precio))

    mesa = Mesa(pedidos)
    mesa.mostrar_pedidos()
    total = mesa.calcular_total()
    print("Precio total de mesa: $", total)

# La estructura de datos utilizada para almacenar la información es una lista de objetos Pedido. Cada objeto contiene el número y el precio de un pedido.
"""
# 2)
"""
class Pared :
    def __init__(self, alto: float, ancho: float):
        self.alto = alto
        self.ancho = ancho

    def superficie_pared(self) -> float:
        return self.alto * self.ancho

class Habitacion :
    def __init__(self):
        self.paredes = []
        self.aberturas = []
    
    def agregar_pared(self, pared: Pared):
        self.paredes.append(pared)

    def agregar_apertura(self, largo: float, alto: float):
        self.aberturas.append((largo, alto))
    
    def superficie_total(self) -> float:
        total_paredes = sum(pared.superficie_pared() for pared in self.paredes)
        total_aberturas = sum(largo * alto for largo, alto in self.aberturas)
        return total_paredes - total_aberturas
    
    def litros_pintura(self, rendimiento_litro_m2: float = 10) -> float:
        return self.superficie_total() / rendimiento_litro_m2

if __name__ == "__main__":
    habitacion = Habitacion()
    for i in range(1, 5):
        print(f"Ingrese datos para la pared {i}:")
        alto = float(input("Alto (m): "))
        ancho = float(input("Ancho (m): "))
        pared = Pared(alto, ancho)
        habitacion.agregar_pared(pared)
        
        tiene_apertura = input("¿La pared tiene apertura? (s/n): ").strip().lower()
        if tiene_apertura == 's':
            largo_apertura = float(input("Largo de la apertura (m): "))
            alto_apertura = float(input("Alto de la apertura (m): "))
            habitacion.agregar_apertura(largo_apertura, alto_apertura)
    
    superficie = habitacion.superficie_total()
    pintura = habitacion.litros_pintura()
    
    print(f"Superficie total a pintar: {superficie} m²")
    print(f"Litros de pintura necesarios (rendimiento 10 m²/litro): {pintura} litros")
"""
# 3)
"""
class Pais:
    def __init__(self, nombre: str, capital: str, poblacion: int):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = []

    def agregar_limitrofe(self, otro_pais):
        if otro_pais not in self.limitrofes:
            self.limitrofes.append(otro_pais)
            otro_pais.agregar_limitrofe(self)

    def obtener_limitrofes(self):
        nombres_limitrofes = []
        for pais in self.limitrofes:
            nombres_limitrofes.append(pais.nombre)
        return nombres_limitrofes
    
if __name__ == "__main__":
    paises = {}

    cantidad = int(input("¿Cuántos países desea cargar?: "))
    for i in range(cantidad):
        nombre = input("Nombre del país: ").strip()
        capital = input(f"Capital de {nombre}: ").strip()
        poblacion = int(input(f"Población de {nombre}: "))
        paises[nombre] = Pais(nombre, capital, poblacion)
        
    seguir_agregando = True
    while seguir_agregando:
        pais_nombre = input("Agregar un limítrofe al pais: (o 'fin' para terminar): ").strip()
        if pais_nombre.lower() == 'fin':
            seguir_agregando = False
        else:
            if pais_nombre in paises:
                lim_nombre = input(f"Ingrese el nombre del país limítrofe a {pais_nombre}: ").strip()
                if lim_nombre in paises:
                    paises[pais_nombre].agregar_limitrofe(paises[lim_nombre])
                    print(f"{lim_nombre} agregado como limítrofe de {pais_nombre}.")
                else:
                    print("Ese país limítrofe no fue cargado.")
            else:
                print("Ese país no fue cargado.")

    pais_a_mostrar = input("¿De qué país desea ver los limítrofes?: ").strip()
    
    if pais_a_mostrar in paises:
        lim = paises[pais_a_mostrar].obtener_limitrofes()
        if lim:
            print(f"Países limítrofes de {pais_a_mostrar}: {', '.join(lim)}")
        else:
            print(f"{pais_a_mostrar} no tiene países limítrofes cargados.")
    else:
        print("Ese país no fue cargado.")
"""