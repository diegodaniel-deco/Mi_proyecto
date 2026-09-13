def validar_texto_obligatorio(texto):
    return texto is not None and texto.strip() != ""
 
 
def validar_codigo_estudiante(codigo, longitud_minima=6):
    return validar_texto_obligatorio(codigo) and len(codigo.strip()) >= longitud_minima  # sin el strip() aca, un codigo de puros espacios pasaba igual
 
 
# tipos de consulta que acepta el sistema (los mismos que salen en el enunciado)
TIPOS_CONSULTA_VALIDOS = ["matricula", "pagos", "constancia", "plataforma", "otro"]
 
 
def validar_tipo_consulta(tipo):
    return tipo.strip().lower() in TIPOS_CONSULTA_VALIDOS
 
 
def asignar_prioridad(tipo_consulta):
    tipo = tipo_consulta.strip().lower()
    if tipo in ("plataforma", "matricula"):
        return "Alta"
    elif tipo == "pagos":
        return "Media"
    else:
        return "Baja"
 
 
def mostrar_menu():
    print("\n--- Soporte Academico ---")
    print("1. Registrar solicitud")
    print("2. Salir")
 
 
def mostrar_resumen(solicitud):
    print("\nResumen de la solicitud registrada:")
    print(f"Codigo: {solicitud['codigo']}")
    print(f"Nombre: {solicitud['nombre']}")
    print(f"Tipo de consulta: {solicitud['tipo']}")
    print(f"Descripcion: {solicitud['descripcion']}")
    print(f"Prioridad asignada: {solicitud['prioridad']}")
 
 
def registrar_solicitud():
    codigo = input("Codigo de estudiante: ")
    if not validar_codigo_estudiante(codigo):
        print("Codigo invalido. Debe tener al menos 6 caracteres.")
        return None
 
    nombre = input("Nombre: ")
    if not validar_texto_obligatorio(nombre):
        print("El nombre no puede estar vacio.")
        return None
 
    tipo = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ")
    if not validar_tipo_consulta(tipo):
        print("Tipo de consulta no reconocido.")
        return None
 
    descripcion = input("Descripcion breve: ")
    prioridad = asignar_prioridad(tipo)
 
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.strip().lower(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad,
    }
    # print(solicitud)  # esto lo dejamos aca de cuando probabamos, ya no hace falta pero no lo borramos por si acaso
    return solicitud
 
 
def main():
    solicitudes_registradas = []
    while len(solicitudes_registradas) < 3:  # de momento lo dejamos en 3 nomas para las pruebas del lab
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            nueva = registrar_solicitud()
            if nueva:
                solicitudes_registradas.append(nueva)
                mostrar_resumen(nueva)
        elif opcion == "2":
            break
        else:
            print("Opcion no valida.")  # TODO: explicar mejor que opciones hay (pendiente segun el feedback)
 
    print(f"\nTotal de solicitudes registradas: {len(solicitudes_registradas)}")
 
 
if __name__ == "__main__":
    main()
