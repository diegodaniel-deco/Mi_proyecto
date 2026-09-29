class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad
