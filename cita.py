from paciente import Paciente
from medico import Medico

class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    def resumen(self):
        return f"Código de cita: CIT-{self._codigo}\n" \
        f"Código del paciente: PAC-{self._paciente.codigo}\n" \
        f"Nombre del paciente: {self._paciente.nombre}\n" \
        f"Edad del paciente: {self._paciente.edad}\n" \
        f"Código del médico: {self._medico.codigo}\n" \
        f"Médico/a: Dr. {self._medico.nombre}\n" \
        f"Área de Especialidad: {self._medico.especialidad}\n" \
        f"Fecha seleccionada para la cita: {self._fecha}"

medicos = [
    Medico("MED-001", "Luis Ramos", "Nutrición"),
    Medico("MED-002", "Ana Torres", "Psicología"),
    Medico("MED-003", "Carlos Pérez", "Odontología"),
    Medico("MED-004", "María Flores", "Cardiología"),
    Medico("MED-005", "Pedro Sánchez", "Pediatría")
]

pacientes = [
    Paciente("123", "Alessandro Anthony", 19),
    Paciente("098", "Diego Daniel", 18),
    Paciente("836", "Jorge Joaquin", 17),
    Paciente("086", "Rootney Alessandro", 17),
    Paciente("777", "Junior Jerao", 17)
]

citas = [
    Cita("001", pacientes[0], medicos[0], "30/09/2026"),
    Cita("002", pacientes[1], medicos[1], "01/10/2026"),
    Cita("003", pacientes[2], medicos[2], "02/10/2026"),
    Cita("004", pacientes[3], medicos[3], "03/10/2026"),
    Cita("005", pacientes[4], medicos[4], "04/10/2026")
]

def seleccionar_opcion():
    print("""
╔══════════════════  BIENVENIDO AL CENTRO DEL CONSULTORIO DEL HOSPITAL  ══════════════════╗
║                                                                                         ║
║   ╔─────────────────────────────────────────────────────────────────────────────────╗   ║
║   │  1. Consultar datos de una cita ........................ seleccione (N. 1)      │   ║
║   │  2. Registrar una cita ................................. seleccione (N. 2)      │   ║
║   ╚─────────────────────────────────────────────────────────────────────────────────╝   ║
║                                                                                         ║
╚═════════════════════════════════════════════════════════════════════════════════════════╝
""")

    alternativa = int(input("Seleccione una opción (con un número): "))

    match alternativa:
        case 1:
            return 1
        case 2:
            return 2
        case _:
            print("La opción seleccionada no es válida")
            return 0


def elegir_medico():
    print("\n====== ÁREAS DEL HOSPITAL ======")
    print("1. Nutrición")
    print("2. Psicología")
    print("3. Odontología")
    print("4. Cardiología")
    print("5. Pediatría")

    opcion = int(input("Seleccione un área del hospital (con un número): "))

    match opcion:
        case 1:
            return medicos[0]
        case 2:
            return medicos[1]
        case 3:
            return medicos[2]
        case 4:
            return medicos[3]
        case 5:
            return medicos[4]
        case _:
            print("Opción inválida")
            exit()


def generar_cita():
    nuevas_citas = []
    continuar = True
    while continuar:
        print("\n===== REGISTRO DEL PACIENTE =====")
        codigo_cita = input("Ingrese código de la cita CIT-(MAX. 3 dígitos): ")
        codigo = input("Ingrese código del paciente PAC-(MAX. 3 dígitos): ")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingresar edad: "))
        paciente = Paciente(codigo, nombre, edad)
        medico=elegir_medico()
        fecha = input("Ingresar fecha en la que desea reservar una cita (dd/mm/aaaa): ")
        cita = Cita(codigo_cita, paciente, medico, fecha)
        nuevas_citas.append(cita)
        continuar=input("\n¿Desea registrar otra cita? (si/no): ").lower()=="si"

    print("\n===== RESUMEN DE CITAS REGISTRADAS =====")
    for cita in nuevas_citas:
        print(cita.resumen())
        print("\n=================================")
    return nuevas_citas

def buscar_por_codigo(citas):
    print("\n========== BÚSQUEDA DE CITAS REGISTRADAS ==========")
    codigo = input("\nIngrese el código de la cita CIT-: ")
    for cita in citas:
        if cita.codigo == codigo:
            print("\n===== CITA ENCONTRADA =====")
            print(cita.resumen())
            return

    print("\nNo se encontró ninguna cita con ese código.")
