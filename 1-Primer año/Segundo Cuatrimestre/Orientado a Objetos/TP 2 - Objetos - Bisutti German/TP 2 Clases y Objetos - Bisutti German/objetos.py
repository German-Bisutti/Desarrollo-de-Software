#
# TP 1 Clases y Objetos
#1) Implementar Linked List con objetos. Cada nodo de la Linked List debe almacenar un dato, este puede ser
#un int, un float, un string o del tipo que deseen. Se deben crear, como mínimo, los siguientes métodos los
#para trabajar con los datos. Pueden implementar métodos adicionales si lo necesitan o desean.
#NOTA: No pueden utilizar una lista como estructura de datos, es decir no se pueden guardar todos los
#datos en una lista que se utiliza como una Linked List.
#• Agregar (dato) -> None: Agrega un nuevo dato a la Linked List. Se puede agregar al inicio, al final
#de la lista o, si se desea, agregarla de forma que la Linked List quede ordenada.
#• Buscar (dato) -> Bool: Busca un dato en la Linked List. Si el dato está, devuelve True, sino, False.
#Alternativamente la función puede devolver el nodo que contiene el dato buscado.
#• Borrar (dato) -> LinkedList: Elimina un nodo de la Linked List que contiene el dato suministrado.
#• Listar () -> list[dato]: Devuelve una lista con todos los datos de la Linked List.

#2) Implementar Binary Tree con objetos. Cada nodo del Binary Tree debe almacenar un dato, este puede ser
#un int, un float, un string o de cualquier tipo que implemente los métodos < y > (mayor y menor). Se deben
#crear, como mínimo, los siguientes métodos los para trabajar con los datos. Pueden implementar métodos
#adicionales si lo necesitan o desean.
#• Agregar (dato) -> None: Agrega un nuevo dato al Binary Tree. Se debe agregar de forma que el
# Binary Tree quede ordenado.
#• Buscar (dato) -> Bool: Busca un dato en la Binary Tree. Si el dato está, devuelve True, sino, False.
# Alternativamente la función puede devolver el nodo que contiene el dato buscado.
#• Borrar (dato) -> BinaryTree: Elimina un nodo de la Binary Tree que contiene el dato suministrado.
#• Listar () -> list[dato]: Devuelve una lista con todos los datos de la Binary Tree ordenados.

#3) Realizar un archivo de testeo (unttest) para las estructuras de datos anteriores (un archivo de testeo para
#cada estructura). El test debe verificar el correcto funcionamiento de los métodos requeridos en cada
#estructura de datos.

#1)

class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.hijo = None

class LinkedList:
    def __init__(self):
        self.padre = None

    def agregar(self, valor: int) -> None:
        nuevo = Nodo(valor)
        if self.padre is None or valor < self.padre.valor:
            nuevo.hijo = self.padre
            self.padre = nuevo
            return
        
        actual = self.padre

        while actual.hijo is not None and actual.hijo.valor < valor:
            actual = actual.hijo

        nuevo.hijo = actual.hijo
        actual.hijo = nuevo

    def buscar(self, valor: int) -> bool:
        actual = self.padre
        while actual is not None:
            if actual.valor == valor:
                return True
            actual = actual.hijo
        return False
                 
    def borrar(self, valor: int):
        actual = self.padre
        anterior = None

        while actual is not None:
            if actual.valor == valor:
                if anterior is None:
                    self.padre = actual.hijo
                else:
                    anterior.hijo = actual.hijo
                return True
            anterior = actual
            actual = actual.hijo
        
        return False
    
    def listar(self) -> list:
        actual = self.padre
        lista = []
        while actual is not None:
            lista.append(actual.valor)
            actual = actual.hijo
        return lista

def menu():
    lista = LinkedList()

    while True:
        print("\n--- MENÚ ---")
        print("\n1. Agregar valor")
        print("\n2. Buscar valor")
        print("\n3. Borrar valor")
        print("\n4. Listar valores")
        print("\n5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            valor = int(input("Ingresá un número: "))
            lista.agregar(valor)
            print("Agregado correctamente.")
        elif opcion == "2":
            valor = int(input("Número a buscar: "))
            encontrado = lista.buscar(valor)
            if encontrado:
                print("Está en la lista." )
            else:
                print("No se encontró.")
        elif opcion == "3":
            valor = int(input("Número a borrar: "))
            borrado = lista.borrar(valor)
            if borrado:
                print("Borrado exitosamente." )
            else:
                print("No se encontró para borrar.")
        elif opcion == "4":
            print("Contenido de la lista:", lista.listar())
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

#2)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.mayor = None
        self.menor = None

class BinaryTree:
    def __init__(self):
        self.padre = None
    
    def agregar(self, valor: int) -> None:
        nuevo = Nodo(valor)
        if self.padre is None:
            self.padre = nuevo
            return
        actual = self.padre
        while True:
            if valor < actual.valor:
                if actual.menor is None:
                    actual.menor = nuevo
                    return
                else:
                    actual = actual.menor
            elif valor > actual.valor:
                if actual.mayor is None:
                    actual.mayor = nuevo
                    return
                else:
                    actual = actual.mayor
            else:
                return
    
    def buscar(self, valor: int) -> bool:
        actual = self.padre
        while actual is not None:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.menor
            else:
                actual = actual.mayor
        return False
    
    def borrar(self, valor: int):
        actual = self.padre
        padre = None
        es_menor = True

        while actual is not None and actual.valor != valor:
            padre = actual
            if valor < actual.valor:
                es_menor = True
                actual = actual.menor
            else:
                es_menor = False
                actual = actual.mayor

        if actual is None:
            return False
        
        if actual.menor is None and actual.mayor is None:
            if actual == self.padre:
                self.padre = None
            elif es_menor:
                padre.menor = None
            else:
                padre.mayor = None

        elif actual.menor is None:
            if actual == self.padre:
                self.padre = actual.mayor
            elif es_menor:
                padre.menor = actual.mayor
            else:
                padre.mayor = actual.mayor
        
        elif actual.mayor is None:
            if actual == self.padre:
                self.padre = actual.menor
            elif es_menor:
                padre.menor = actual.menor
            else:
                padre.mayor = actual.menor

        else:
            sucesor_padre = actual
            sucesor = actual.mayor
            while sucesor.menor is not None:
                sucesor_padre = sucesor
                sucesor = sucesor.menor
            
            actual.valor = sucesor.valor
            if sucesor_padre == actual:
                sucesor_padre.mayor = sucesor.mayor
            else:
                sucesor_padre.menor = sucesor.mayor
        
        return True
    
    def listar(self) -> list:
        def recorrer_en_orden(nodo):
            if nodo is None:
                return []
            else:
                return recorrer_en_orden(nodo.menor) + [nodo.valor] + recorrer_en_orden(nodo.mayor)
        return recorrer_en_orden(self.padre)

def menu():
    arbol = BinaryTree()
    seguir = True

    while seguir:
        print("\n--- MENÚ ---")
        print("1. Agregar valor")
        print("2. Buscar valor")
        print("3. Borrar valor")
        print("4. Listar valores ordenados")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            valor = int(input("Ingresá un número: "))
            arbol.agregar(valor)
            print("Agregado correctamente.")
        elif opcion == "2":
            valor = int(input("Número a buscar: "))
            if arbol.buscar(valor):
                print("El número está en el árbol.")
            else:
                print("El número no se encontró.")
        elif opcion == "3":
            valor = int(input("Número a borrar: "))
            if arbol.borrar(valor):
                print("Borrado exitosamente.")
            else:
                print("No se encontró el valor para borrar.")
        elif opcion == "4":
            lista = arbol.listar()
            if lista:
                print("Contenido del árbol (ordenado):", lista)
            else:
                print("Árbol vacío.")
        elif opcion == "5":
            print("Saliendo del programa.")
            seguir = False
        else:
            print("Opción inválida. Por favor, elegí del 1 al 5.")

if __name__ == "__main__":
    menu()
