
class Cliente:
    def __init__(self, nombre, codigo_cliente, telefono):
        self._nombre = nombre
        self._codigo_cliente = codigo_cliente
        self._telefono = telefono

class Plato:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

class Pedido:
    def __init__(self, cliente, codigo):
        self._cliente = cliente
        self._platos = []
        self._codigo = codigo

class Restaurante:
    def __init__(self, nombre):
        self._nombre = nombre
        self._pedidos = []

class Extra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

platos = [
    Plato("1 Pollo a la brasa", 60),
    Plato("1/2 pollo", 32),
    Plato("1/4 de pollo", 18),
    Plato("1/8 de pollo", 14),
    Plato("1 Cubeta de pollo broaster", 60),
    Plato("Mini cubeta de pollo broaster", 30),
    Plato("Big crunch", 15),
    Plato("Menu universitario", 12)
]

extras = [
    Extra("Porción de papas", 10),
    Extra("Limonada", 2),
    Extra("Chicha morada", 3),
    Extra("Ensalada", 5),
    Extra("Gaseosa 1L", 10),
    Extra("Gaseosa 1/2L", 8),
    Extra("Gaseosa personal", 2)
]

clientes = []
restaurante = Restaurante("Los Pollos Hermanos")

def seleccionar_opcion():
    print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                ║
║                         BIENVENIDO AL SISTEMA DEL RESTAURANTE                                  ║
║                                                                                                ║
║   ╔────────────────────────────────────────────────────────────────────────────────────────╗   ║
║   │                                                                                        │   ║
║   │   1. Registrar cliente ..................................... Seleccione (N. 1)         │   ║
║   │   2. Realizar pedido ....................................... Seleccione (N. 2)         │   ║
║   │   3. Consultar pedido ...................................... Seleccione (N. 3)         │   ║
║   │   4. Consultar mesas disponibles .......................... Seleccione (N. 4)          │   ║
║   │   5. Listar y ordenar información ......................... Seleccione (N. 5)          │   ║
║   │   6. Liberar mesa .......................................... Seleccione (N. 6)         │   ║
║   │   7. Salir ................................................. Seleccione (N. 7)         │   ║
║   │                                                                                        │   ║
║   ╚────────────────────────────────────────────────────────────────────────────────────────╝   ║
║                                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

    opcion = int(input("Seleccione una opción: "))
    match opcion:
        case 1:
            registro_cliente()
        case 2:
            toma_pedido()
        case 3:
            consultar_pedido()
        case 4:
            print("Opción pendiente")
        case 5:
            print("Opción pendiente")
        case 6:
            print("Función pendiente)
        case 7:
            print("Gracias por utilizar nuestro sistema.")
            return False
        case _:
            print("Opción incorrecta.")
    return True

def registro_cliente():
    print("""
╔═════════════════════════════════════════════╗
║   REGISTRO DE CLIENTE/LOS POLLOS HERMANOS   ║
╚═════════════════════════════════════════════╝
""")

    nombre = input("Ingresar nombre del cliente: ")
    codigo_cliente = int(input("Asignar un código: "))
    telefono = input("Ingresar número de contacto: ")
    for cliente in clientes:
        if cliente._codigo_cliente == codigo_cliente:
        print("Este codigo ya a sido registrado")
        return
    cliente = Cliente(nombre, codigo_cliente, telefono)
    clientes.append(cliente)
    print("Cliente registrado correctamente.")

def mostrar_menu(pedido_actual):
while True:
        print("""
╔════════════════════════════════════════════════════╗
║              LOS POLLOS HERMANOS                   ║
║                   MENÚ DE PLATOS                   ║
╠════════════════════════════════════════════════════╣
║  N.°   PLATO                              PRECIO   ║
╠════════════════════════════════════════════════════╣
║   1.   1 Pollo a la brasa                 S/ 60.00 ║
║   2.   1/2 pollo                          S/ 32.00 ║
║   3.   1/4 de pollo                       S/ 18.00 ║
║   4.   1/8 de pollo                       S/ 14.00 ║
║   5.   1 Cubeta de pollo broaster         S/ 60.00 ║
║   6.   Mini cubeta de pollo broaster      S/ 30.00 ║
║   7.   Big crunch                         S/ 15.00 ║
║   8.   Menú universitario                 S/ 12.00 ║
╠════════════════════════════════════════════════════╣
║   0.   Terminar selección de platos                ║
╚════════════════════════════════════════════════════╝
""")

    plato_seleccionado = int(input("Seleccione un plato (1-8) o (0 para terminar el listado): "))
     if plato_seleccionado == 0:
            if len(pedido_actual) == 0:
                print("Primero debe seleccionar un plato.")
            else:
                break
    if 1 <= plato_seleccionado <= len(platos):
        cant_plato = int(input("Indique la cantidad: "))
        if cant_plato > 0:
            plato = platos[plato_seleccionado - 1]
            subtotal = plato._precio * cant_plato
            pedido_actual.append((plato, cant_plato, subtotal))
            print("\nPLATO SELECCIONADO")
            print(f"Plato: {plato._nombre}")
            print(f"Cantidad: {cant_plato}")
            print(f"Subtotal: S/{subtotal:.2f}")
            print("\nPlato agregado correctamente")
        else:
            print("La cantidad debe ser mayor a cero.")
    else:
        print("El plato seleccionado no existe.")

def toma_pedido():
    print("""
╔════════════════════════════════════════════════════╗
║                   TOMA DE PEDIDO                   ║
╚════════════════════════════════════════════════════╝
""")

    if len(clientes) == 0:
        print("Primero debe registrar un cliente.")
        return
    print("CLIENTES REGISTRADOS")
    for cliente in clientes:
        print(
            f"Código: {cliente._codigo_cliente} | "
            f"Nombre: {cliente._nombre}"
        )
    codigo_cliente = int(input("\nIngrese el código del cliente: "))
    cliente_encontrado = buscar_cliente(codigo_cliente)
    if cliente_encontrado is None:
        print("No se encontró al cliente.")
        return
    pedido_actual = []
    mostrar_menu(pedido_actual)
    print("""
╔════════════════════════════════════════════════════╗
║              RESUMEN DEL PEDIDO                    ║
╚════════════════════════════════════════════════════╝
""")
    total = 0
    for plato, cantidad, subtotal in pedido_actual:
        print(f"Plato: {plato._nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Subtotal: S/ {subtotal:.2f}")
        print("--------------------------------------")
        total += subtotal
    print(f"Cliente: {cliente_encontrado._nombre}")
    print(f"Código de cliente: {cliente_encontrado._codigo_cliente}")
    print(f"TOTAL A PAGAR: S/ {total:.2f}")
    confirmar = input(
        "\n¿Este es el pedido que desea registrar? (si/no): ").lower()
    if confirmar == "si":
        codigo_pedido = len(restaurante._pedidos) + 1
        pedido = Pedido(cliente_encontrado, codigo_pedido)
        pedido._platos.extend(pedido_actual)
        restaurante._pedidos.append(pedido)
        print("""
╔════════════════════════════════════════════════════╗
║                 REGISTRO EXITOSO                   ║
╚════════════════════════════════════════════════════╝
""")
        print(f"Código del pedido: PED-{codigo_pedido:03d}")
        print(f"Cliente: {cliente_encontrado._nombre}")
        print(f"Total registrado: S/ {total:.2f}")
    else:
        print("\nEl pedido no fue registrado.")

def consultar_pedido():
    print("""
╔════════════════════════════════════════════════════╗
║                 CONSULTAR PEDIDO                   ║
╚════════════════════════════════════════════════════╝
""")
    if len(restaurante._pedidos) == 0:
        print("No existen pedidos registrados.")
        return
    codigo = int(input("Ingrese el número del pedido: "))
    encontrado = False
    for pedido in restaurante._pedidos:
        if pedido._codigo == codigo:
            encontrado = True
            print(f"\nCódigo del pedido: PED-{pedido._codigo:03d}")
            print(f"Cliente: {pedido._cliente._nombre}")
            print(f"Código del cliente: {pedido._cliente._codigo_cliente}")
            print("--------------------------------------")
            total = 0
            for plato, cantidad, subtotal in pedido._platos:
                print(f"Plato: {plato._nombre}")
                print(f"Cantidad: {cantidad}")
                print(f"Subtotal: S/ {subtotal:.2f}")
                print("--------------------------------------")
                total += subtotal
            print(f"TOTAL A PAGAR: S/ {total:.2f}")
            break
    if encontrado == False:
        print("No se encontró el pedido.")

while True:
    continuar = seleccionar_opcion()
    if continuar == False:
        break
