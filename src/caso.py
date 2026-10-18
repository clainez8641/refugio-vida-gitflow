from abc import ABC, abstractmethod
from datetime import datetime

from estados import Rescatado


class Animal(ABC):
    def __init__(self, nombre="Sin nombre"):
        self.nombre = nombre

    @abstractmethod
    def especie(self):
        pass


class Perro(Animal):
    def especie(self):
        return "perro"


class Gato(Animal):
    def especie(self):
        return "gato"


class FaunaSilvestre(Animal):
    def especie(self):
        return "fauna silvestre"


class Caso:
    _contador = 0

    def __init__(self, ubicacion, descripcion, animal, foto=None):
        Caso._contador += 1
        self.id = f"CR-{Caso._contador:03d}"
        self.fecha = datetime.now()
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.animal = animal
        self.foto = foto
        self.estado = Rescatado()
        self.responsable = None
        self.alta_medica = False
        self.adopcion_aprobada = False
        self.historial = []

    def nombre_estado(self):
        return type(self.estado).__name__

    def avanzar(self, usuario="sistema"):
        """Delega en el estado actual y registra la transición (REQ-N04)."""
        anterior = self.nombre_estado()
        self.estado.avanzar(self)
        nuevo = self.nombre_estado()
        if anterior != nuevo:
            self.historial.append((datetime.now(), usuario, anterior, nuevo))
