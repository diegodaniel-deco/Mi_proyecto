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
        return f"Código de cita: {self._codigo}\n" \
        f"Código del paciente: PAC-{self._paciente.codigo}\n" \
        f"Nombre del paciente: {self._paciente.nombre}\n" \
        f"Edad del paciente: {self._paciente.edad}\n"\
        f"Código del médico: {self._medico.codigo}\n" \
        f"Médico/a : Dr. {self._medico.nombre}\n" \
        f"Área de Especialidad: {self._medico.especialidad}\n" \
        f"Fecha seleccionada: {self._fecha}"
       


medicos = [
    Medico("MED-001", "Luis Ramos", "Nutrición"),
    Medico("MED-002", "Ana Torres", "Psicología"),
    Medico("MED-003", "Carlos Pérez", "Odontología"),
    Medico("MED-004", "María Flores", "Cardiología"),
    Medico("MED-005", "Pedro Sánchez", "Pediatría")
]


def elegir_medico():

    print("\n======ÁREAS DEL HOSPITAL======")
    print("1. Nutrición")
    print("2. Psicología")
    print("3. Odontología")
    print("4. Cardiología")
    print("5. Pediatría")

    opcion = int(input("Seleccione una área del hospital(con un número): "))

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
            print("Opción invalida")
            exit()


def generar_cita():

    print("\n=====REGISTRO DEL PACIENTE=====")

    codigo = input("Ingrese código del paciente PAC-:")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingresar edad: "))
    paciente = Paciente(codigo, nombre, edad)
    medico = elegir_medico()
    fecha = input("Ingresar fecha en la que desea reservar una cita(dd/mm/aaaa): ")
    cita = Cita("CIT-001", paciente, medico, fecha)

    print("\n--- RESUMEN DE LA CITA ---")
    print(cita.resumen())

    return cita