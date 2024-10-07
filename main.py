def cargarProducto(nombreProducto, precioProducto, stockProducto):
    listaCargado = []
    listaCargado.append(nombreProducto)
    listaCargado.append(precioProducto)
    listaCargado.append(stockProducto)
    return listaCargado

def buscarProducto(productoBuscar):
    productoEncontrado = []
    for i in range(len(inventario)):
        if inventario[i][0] == productoBuscar:
            productoEncontrado.append(inventario[i][0])
            productoEncontrado.append(inventario[i][1])
            productoEncontrado.append(inventario[i][2])
            return productoEncontrado
        else:
            print("El producto no se encontro.")

def ordenarInventario(inventario):
    longitud = (len(inventario))

    for i in range(longitud):
        for j in range(longitud - 1 - i):
            if inventario[j] < inventario[j+1]:
                temp = inventario[j+1]
                inventario[j+1] = inventario[j]
                inventario[j] = temp
    return inventario

def buscarMasCaro(inventario):
    pass

def buscarsMasBarato(inventario):
    pass

def buscarMayores15000(inventario):
    pass

inventario = []

continuar = "1"

while continuar == "1":

    print("Menu Principal:")
    print("[1] Cargar Producto")
    print("[2] Buscar Producto")
    print("[3] Ordenar Inventario")
    print("[4] Producto mas Caro")
    print("[5] Producto mas Barato")
    print("[6] Productos Mayor 15000")
    print("[7] Salir")
    opcionElegida = int(input("Respuesta: "))

    if opcionElegida == 1:
        nombreProducto = input("Ingrese el nombre del producto: ")
        precioProducto = float(input("Ingrese el precio del producto: "))
        stockProducto = int(input("Ingrese stock del producto: "))
        nuevoProducto = cargarProducto(nombreProducto, precioProducto, stockProducto)
        inventario.append(nuevoProducto)
        print(f"Nuevo producto cargado: {nombreProducto}")
    elif opcionElegida == 2:
        productoBuscar = input("Ingrese el nombre del producto a buscar: ")
        productoEncontrado = buscarProducto(productoBuscar)
        print(f"Producto encontrado: {productoEncontrado[0]}")
        print(f"Precio: {productoEncontrado[1]}")
        print(f"Stock: {productoEncontrado[2]}")
    elif opcionElegida == 3:
        inventarioOrdenado = ordenarInventario(inventario)
        print(inventarioOrdenado)
    elif opcionElegida == 4:
        productoMasCaro = buscarMasCaro(inventario)
        print(f"Producto mas Caro: ")
        print(f"Precio: ")

    print("")
    print("[1] Menu Principal")
    print("[2] Salir")
    seguir = input("Respuesta: ")
    if seguir == "1":
        continuar = "1"
    else:
        continuar = False