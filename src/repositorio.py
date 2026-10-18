class RepositorioCasos:
    def __init__(self):
        self._casos = []

    def guardar(self, caso):
        self._casos.append(caso)

    def buscar(self, id_caso):
        for c in self._casos:
            if c.id == id_caso:
                return c
        return None

    def filtrar(self, especie=None, estado=None, encargado=None):
        resultado = self._casos
        if especie:
            resultado = [c for c in resultado if c.animal.especie() == especie]
        if estado:
            resultado = [c for c in resultado if c.nombre_estado() == estado]
        if encargado:
            resultado = [c for c in resultado if c.responsable is encargado]
        return resultado
