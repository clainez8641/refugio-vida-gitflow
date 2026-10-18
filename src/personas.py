class Persona:
    def __init__(self, nombre, especialidad=None):
        self.nombre = nombre
        self.especialidad = especialidad
        self.casos_activos = 0

    def __repr__(self):
        return self.nombre


class Voluntario(Persona):
    pass


class Veterinario(Persona):
    pass


class Coordinador(Persona):
    pass
