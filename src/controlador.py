from asignacion import AsignadorEncargado
from caso import Caso
from estados import TransicionNoPermitida


class CasoControlador:
    def __init__(self, repositorio, vista, publicador):
        self._repositorio = repositorio
        self._vista = vista
        self._publicador = publicador

    def reportar(self, datos):
        caso = Caso(**datos)
        self._repositorio.guardar(caso)       # primero se guarda (REQ-N05)
        self._publicador.notificar(caso)
        self._vista.mostrar_confirmacion(caso.id)
        return caso

    def avanzar_caso(self, id_caso, usuario):
        caso = self._repositorio.buscar(id_caso)
        try:
            caso.avanzar(usuario)
        except TransicionNoPermitida as error:
            self._vista.mostrar_error(str(error))

    def asignar_encargado(self, caso, candidatos, estrategia):
        AsignadorEncargado(estrategia).asignar(caso, candidatos)
        self._vista.mostrar_confirmacion(caso.id)

    def consultar(self, **filtros):
        self._vista.mostrar_casos(self._repositorio.filtrar(**filtros))
