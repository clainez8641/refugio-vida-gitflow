class CasoVista:
    def mostrar_confirmacion(self, id_caso):
        print(f">> Reporte recibido. Número de caso: {id_caso}")

    def mostrar_casos(self, casos):
        for c in casos:
            responsable = c.responsable or "sin asignar"
            print(f"{c.id} | {c.animal.especie():15} | {c.nombre_estado():13} | {responsable}")

    def mostrar_error(self, mensaje):
        print(f"!! {mensaje}")
