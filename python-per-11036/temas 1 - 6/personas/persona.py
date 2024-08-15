class Persona:
    '''Refresenta una persona.'''

    def __init__(self, nombre, fecha_de_nacimiento, domicilio) -> None:
        '''Constructor de la clase Persona.'''
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.domicilio = domicilio

    def cambiar_domicilio(self, nuevo_domicilio):
        self.domicilio = nuevo_domicilio
