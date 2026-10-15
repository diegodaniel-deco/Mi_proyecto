
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


def seleccionar_opcion():
    print("""
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                ║
║                         BIENVENIDO AL SISTEMA DEL RESTAURANTE                                  ║
║                                                                                                ║
║   ╔────────────────────────────────────────────────────────────────────────────────────────╗   ║
║   │                                                                                        │   ║
║   │   1. Registrar cliente ..................................... Seleccione (N. 1)         │   ║
║   │   2. Ver menú de platos .................................... Seleccione (N. 2)         │   ║
║   │   3. Realizar pedido ....................................... Seleccione (N. 3)         │   ║
║   │   4. Consultar pedido ...................................... Seleccione (N. 4)         │   ║
║   │   5. Consultar mesas disponibles .......................... Seleccione (N. 5)         │   ║
║   │   6. Listar y ordenar información .......................... Seleccione (N. 6)         │   ║
║   │   7. Liberar mesa .......................................... Seleccione (N. 7)         │   ║
║   │   8. Salir ................................................. Seleccione (N. 8)         │   ║
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
            mostrar_menu()

        case 3 | 4 | 5 | 6 | 7:
            print("Esta opción se encuentra en desarrollo.")

        case 8:
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

    cliente = Cliente(nombre, codigo_cliente, telefono)

    clientes.append(cliente)

    print("Cliente registrado correctamente.")


def mostrar_menu():
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
╚════════════════════════════════════════════════════╝
""")

    plato_seleccionado = int(input("Seleccione un plato (1-8): "))

    if 1 <= plato_seleccionado <= len(platos):
        cant_plato = int(input("Indique la cantidad: "))

        if cant_plato > 0:
            plato = platos[plato_seleccionado - 1]
            subtotal = plato._precio * cant_plato

            print("\nPLATO SELECCIONADO")
            print(f"Plato: {plato._nombre}")
            print(f"Cantidad: {cant_plato}")
            print(f"Subtotal: S/{subtotal:.2f}")
        else:
            print("La cantidad debe ser mayor a cero.")
    else:
        print("El plato seleccionado no existe.")


# EJECUCIÓN PRINCIPAL

while True:
    continuar = seleccionar_opcion()

    if continuar == False:
        break
