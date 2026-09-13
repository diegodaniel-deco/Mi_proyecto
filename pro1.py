# Lista de servicios disponibles
servicios = ["Matricula", "Pagos", "Constancia", "Plataforma", "Otros", "Salir"]

def mostrar_menu():
    print("===== MENÚ DE SERVICIOS =====")
    for i, servicio in enumerate(servicios):
        print(f"{i+1}. {servicio}")

# Código de estudiante: solo números
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return codigo.isdigit()   #solo números p 

# Nombre: solo letras y espacios
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return nombre.replace(" ", "").isalpha()   #solo letras

def validar_texto(texto):
    return texto.strip() != ""

def calcular_prioridad(tipo):
    match tipo:
        case "Matricula" | "Plataforma":
            return "Alta"
        case "Pagos":
            return "Media"
        case "Constancia":
            return "Baja"
        case "Otros":
            return "Muy baja"
        case _:
            return "Inválida"

def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    print("\n===== RESUMEN =====")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Consulta:", tipo)
    print("Descripción:", descripcion)
    print("Prioridad:", prioridad)
    print("===================\n")

# Programa principal
solicitudes = []

for i in range(1000):  # hasta 1000 solicitudes
    print(f"\n--- Solicitud {i+1} ---")
    codigo = input("Código del estudiante (recuerde solo números): ")
    if not validar_codigo(codigo):
        print("El código debe contener solo números.")
        continue

    nombre = input("Nombre del estudiante (solo letras): ")
    if not validar_nombre(nombre):
        print("El nombre solo debe contener letras.")
        continue

    mostrar_menu()
    opcion = int(input("Seleccione tipo de consulta (con un número) N°: "))
    if opcion == len(servicios):  # opción "Salir"
        print("Finalizando registro de solicitudes...")
        break
    elif opcion < 1 or opcion > len(servicios):
        print("Opción inválida.")
        continue

    tipo_consulta = servicios[opcion - 1]
    descripcion = input("Descripción breve: ")
    if not validar_texto(descripcion):
        print("La descripción es obligatoria.")
        continue

    prioridad = calcular_prioridad(tipo_consulta)
    solicitudes.append((codigo, nombre, tipo_consulta, descripcion, prioridad))
    mostrar_resumen(codigo, nombre, tipo_consulta, descripcion, prioridad)

    continuar = input("¿Desea registrar otra solicitud? (si/no): ").lower()
    if continuar != "si":
        print("Finalizando registro de solicitudes...")
        break

# Mostrar todas las solicitudes
print("\n===== TODAS LAS SOLICITUDES =====")
for s in solicitudes:
    print(s)
