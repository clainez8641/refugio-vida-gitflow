from abc import ABC, abstractmethod


class Suscriptor(ABC):
    @abstractmethod
    def recibir(self, caso):
        pass


class PublicadorRescates:
    def __init__(self):
        self._suscriptores = []

    def suscribir(self, suscriptor):
        self._suscriptores.append(suscriptor)

    def cancelar(self, suscriptor):
        self._suscriptores.remove(suscriptor)

    def notificar(self, caso):
        for s in self._suscriptores:
            try:
                s.recibir(caso)
            except Exception as error:   # REQ-N05: el reporte no se pierde si falla un canal
                print(f"[Aviso] Falló {type(s).__name__}: {error}")


class NotificadorCorreo(Suscriptor):
    def recibir(self, caso):
        print(f"[Correo] Nuevo rescate {caso.id}: {caso.animal.especie()} en {caso.ubicacion}")


class NotificadorSMS(Suscriptor):
    def recibir(self, caso):
        print(f"[SMS] Rescate {caso.id} en {caso.ubicacion}. ¿Quién puede ir?")


class PanelVoluntario(Suscriptor):
    def recibir(self, caso):
        print(f"[Panel] Alerta en pantalla: caso {caso.id} ({caso.descripcion})")
