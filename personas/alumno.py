from persona import Persona


class Alumno(Persona):

    def __init(self, nombre, fecha_de_nacimiento, domicilio, matricula):
        super().__init__(self, nombre, fecha_de_nacimiento, domicilio)
        self.matricula = matricula
        self.calificacion = None

    def calificar(self, calificacion):
        self.calificacion = calificacion
