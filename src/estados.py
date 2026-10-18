from abc import ABC, abstractmethod


class TransicionNoPermitida(Exception):
    pass


class EstadoCaso(ABC):
    @abstractmethod
    def avanzar(self, caso):
        pass


class Rescatado(EstadoCaso):
    def avanzar(self, caso):
        caso.estado = EnTratamiento()


class EnTratamiento(EstadoCaso):
    def avanzar(self, caso):
        if caso.alta_medica:
            caso.estado = EnAdopcion()
        else:
            raise TransicionNoPermitida("Falta el alta médica del veterinario")


class EnAdopcion(EstadoCaso):
    def avanzar(self, caso):
        if caso.adopcion_aprobada:
            caso.estado = Adoptado()
        else:
            raise TransicionNoPermitida("La adopción aún no fue aprobada")


class Adoptado(EstadoCaso):
    def avanzar(self, caso):
        raise TransicionNoPermitida("El caso ya está cerrado")
