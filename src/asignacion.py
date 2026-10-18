from abc import ABC, abstractmethod


class EstrategiaAsignacion(ABC):
    @abstractmethod
    def elegir(self, caso, candidatos):
        pass


class AsignacionPorCarga(EstrategiaAsignacion):
    def elegir(self, caso, candidatos):
        return min(candidatos, key=lambda c: c.casos_activos)


class AsignacionPorEspecialidad(EstrategiaAsignacion):
    def elegir(self, caso, candidatos):
        especie = caso.animal.especie()
        expertos = [c for c in candidatos if c.especialidad == especie]
        return min(expertos or candidatos, key=lambda c: c.casos_activos)


class AsignadorEncargado:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia):
        self._estrategia = estrategia

    def asignar(self, caso, candidatos):
        caso.responsable = self._estrategia.elegir(caso, candidatos)
        caso.responsable.casos_activos += 1
