# Trabajo Practico Desarrollo de Sistemas
# Bisutti German

productos = [(1001, 'Samsung' ,'SG524', 45990, 22),
             (1003, 'Samsung' ,'SA321', 62590, 45),
             (1105, 'LG', 'LG024', 32590, 12),
             (1106, 'LG', 'LG032', 54200, 0),
             (1108, 'LG', 'LG150', 62590, 34),
             (1201, 'SONY', 'ST-321', 85990, 10)]

# 1) Realizar una (o más) función que muestre el listado de productos y permita al usuario seleccionar
# productos. La función recibe el listado de productos y debe devolver una nueva lista de los ID de los
# productos seleccionados.
# Por ejemplo: [1003, 1105, 1201]
'''
def mostrarProductos (productos):
    for producto in productos:
         print("ID:", producto[0], "Nombre:", producto[1], "Modelo:", producto[2], "Precio:", producto[3], "StocK:", producto[4])
    print("---")

# Funcion que imprime info de productos seleccionados 
def listadoId(productos):
    cantidadProductos = int(input("Ingrese el número de productos que quiere seleccionar: "))
    productosId = []
    
    for i in range(cantidadProductos):
        idProducto = int(input("Ingrese el ID del producto: "))
        productosId.append(idProducto)
    
    productosSeleccionados = [producto for producto in productos if producto[0] in productosId]
    mostrarProductos(productosSeleccionados)

# Funcion que imprime id de productos seleccionados Por ejemplo: [1003, 1105, 1201]
def seleccionarProductos(productos):  # Añadir el argumento 'productos'
    cantidadProductos = int(input("Ingrese el número de productos que quiere seleccionar: "))
    productosId = []
    
    for i in range(cantidadProductos):
        idProducto = int(input("Ingrese el ID del producto: "))
        productosId.append(idProducto)
    
    return productosId



mostrarProductos(productos)

listadoId(productos)

productosSeleccionados = seleccionarProductos(productos)
print("IDs de productos seleccionados:", productosSeleccionados)
'''

#2) Realizar una (o más) función que verifique el Stock del producto. La función recibe el listado de
#productor y un id de producto, y debe devolver True si el stock es mayor a 0 y False si el Stock
#es 0.
'''
def stock (producto):
    if producto and producto[4] > 0:
        return True
    elif producto == None:
        return "No existe este producto"


def buscarProducto (productos, ID):
    for p in productos:
        if p[0] == ID:
            return p
    return None

producto1 = buscarProducto(productos, 1201)
producto2 = buscarProducto(productos, 1106)

print("Producto 1 :", stock(producto1))
print("Producto 2 :", stock(producto2))
'''

#3) Realizar una (o más) función que actualice el stock de productos. La función recibe el listado de
#productos y un id de producto. La función puede modificar (actualizar el stock) la lista pasada como
#parámetro o devolver una nueva lista de productos con los valores de stock actualizados
#(respetando la estructura de datos indicada). Opcional, la función puede recibir una lista de IDs (del
#ejercicio 1), y actualizar el stock de todos ellos.
'''
def agregarStock(productos, idProducto, cantidad):

    producto = buscarProducto(productos, idProducto)

    if producto is not None:
        productos[productos.index(producto)] = (producto[0], producto[1], producto[2], producto[3], producto[4] + cantidad)
        return productos
    else:
        print("No existe un producto con ID:", idProducto)
        return productos

def restarStock(productos, idProducto, cantidad):

    producto = buscarProducto(productos, idProducto)
    if producto is not None:
        if producto[4] >= cantidad:
            productos[productos.index(producto)] = (producto[0], producto[1], producto[2], producto[3], producto[4] - cantidad)
            return productos
        else:
            print("No hay suficiente stock para restar:", cantidad)
            return productos
    else:
        print("No existe un producto con ID:", idProducto)
        return productos

def actualizarStock(productos, idProducto):
    accion = input(f"Elija entre sumar o restar stock para el producto con ID {idProducto}? (sumar/restar): ")
    cantidad = int(input("Ingrese la cantidad: "))
    
    if accion == "sumar":
        productos = agregarStock(productos, idProducto, cantidad)
    elif accion == "restar":
        productos = restarStock(productos, idProducto, cantidad)
    else:
        print("Acción no válida. Debe ingresar 'sumar' o 'restar'.")
        return productos

    return productos

mostrarProductos(productos)
productosActualizados = actualizarStock(productos, 1001)
print("Productos actualizados:")
mostrarProductos(productos)
'''
# (1001, 'Samsung' ,'SG524', 45990, 22)

#4) Realizar una (o más) función que calcule el precio total del pedido. La función recibe el listado de
#productos y lista de los ID de los productos seleccionados (del ejercicio 1). La función debe devolver
#el precio total del pedido. Solo debe calcular el precio total con los productos que están en stock. 
'''
def calcularPrecioTotal(productos, productosSeleccionados):
    total = 0
    for idProducto in productosSeleccionados:
        producto = buscarProducto(productos, idProducto)
        if producto and producto[4] > 0:  
            total += producto[3]
    return total

productosSeleccionados = seleccionarProductos(productos)
totalPedido = calcularPrecioTotal(productos, productosSeleccionados)
print("El precio total del pedido es:", totalPedido)
'''
#5) Realizar una (o más) función que muestre el detalle del pedido. La función recibe el listado de
#productos y lista de los ID de los productos seleccionados (del ejercicio 1). La función debe imprimir
#por pantalla marca, modelo y precio unitario de cada producto seleccionado y finalmente el precio
#total del pedido. Descartar del listado los productos fuera de stock. 
'''
def mostrarDetallePedido(productos, productosSeleccionados):
    print("Detalle del Pedido:")
    total = 0
    for idProducto in productosSeleccionados:
        producto = buscarProducto(productos, idProducto)
        if producto and producto[4] > 0:  
            print(f"Marca: {producto[1]}, Modelo: {producto[2]}, Precio Unitario: ${producto[3]}")
            total += producto[3]
    print("---")
    print(f"Precio total del pedido: ${total}")

productosSeleccionados = seleccionarProductos(productos)
mostrarDetallePedido(productos, productosSeleccionados)
'''