from persona import Persona


class Profesor(Persona):
    '''Un profesor or profesora.'''

    def __init__(self, nombre, fecha_de_nacimiento, domicilio, especialidad) -> None:
        super().__init__(nombre, fecha_de_nacimiento, domicilio)

        self.especialidad = especialidad
        self.assignaturas_impartidas = []

    def agregar_asignatura(self, asignatura):
        self.assignaturas_impartidas.append(asignatura)
