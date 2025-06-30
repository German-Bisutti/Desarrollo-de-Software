#
# TP 1 Clases y Objetos
#3) Realizar un archivo de testeo (unttest) para las estructuras de datos anteriores (un archivo de testeo para
#cada estructura). El test debe verificar el correcto funcionamiento de los métodos requeridos en cada
#estructura de datos.

#3)
import unittest
from objetos import LinkedList, BinaryTree

class Test_LinkedList(unittest.TestCase): 
    def test_LinkedList_agregar (self):
        lista = LinkedList()
        lista.agregar(10)
        lista.agregar(20)
        self.assertEqual(lista.listar(), [10, 20])

    def test_LinkedList_buscar (self):
        lista = LinkedList()
        lista.agregar(10)
        lista.agregar(15)
        self.assertTrue(lista.buscar(10))
        self.assertFalse(lista.buscar(20))

    def test_LinkedList_borrar (self):
        lista = LinkedList()
        lista.agregar(10)
        lista.agregar(15)
        self.assertTrue(lista.buscar(10))
        lista.borrar(10)
        self.assertFalse(lista.buscar(10))
        self.assertEqual(lista.listar(), [15])

    def test_LinkedList_listar (self):
        lista = LinkedList()
        self.assertEqual(lista.listar(), [])
        lista.agregar(5)
        lista.agregar(15)
        self.assertEqual(lista.listar(), [5, 15])


class Test_BinaryTree(unittest.TestCase): 
    def test_BinaryTree_agregar (self):
        lista = BinaryTree()
        self.assertEqual(lista.listar(), [])
        lista.agregar(50)
        lista.agregar(40)
        lista.agregar(60)
        self.assertEqual(lista.listar(), [40, 50, 60])
        lista.agregar(45)
        self.assertEqual(lista.listar(), [40, 45, 50, 60])

    def test_BinaryTree_buscar (self):
        lista = BinaryTree()
        self.assertFalse(lista.buscar(40))
        lista.agregar(50)
        lista.agregar(40)
        lista.agregar(60)
        self.assertTrue(lista.buscar(50))
        lista.borrar(50)
        self.assertTrue(lista.buscar(40))
        self.assertTrue(lista.buscar(60))
        self.assertFalse(lista.buscar(70))
        self.assertFalse(lista.buscar(50))

    def test_BinaryTree_borrar (self):
        lista = BinaryTree()
        lista.agregar(50)
        lista.agregar(40)
        lista.agregar(60)
        self.assertTrue(lista.buscar(50))
        self.assertEqual(lista.listar(), [40, 50, 60])
        lista.agregar(55)
        lista.borrar(50)
        self.assertFalse(lista.buscar(50))
        self.assertEqual(lista.listar(), [40, 55, 60])

    def test_BinaryTree_listar (self):
        lista = BinaryTree()
        self.assertEqual(lista.listar(), [])
        lista.agregar(50)
        lista.agregar(40)
        lista.agregar(60)
        self.assertEqual(lista.listar(), [40, 50, 60])
        lista.borrar(50)
        self.assertEqual(lista.listar(), [40, 60])
        lista.borrar(40)
        lista.borrar(60)
        self.assertEqual(lista.listar(), [])
        
if __name__ == "__main__":
    unittest.main()