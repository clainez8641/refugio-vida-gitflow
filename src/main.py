from asignacion import AsignacionPorCarga, AsignacionPorEspecialidad
from caso import FaunaSilvestre, Gato, Perro
from controlador import CasoControlador
from notificaciones import NotificadorCorreo, NotificadorSMS, PanelVoluntario, PublicadorRescates
from personas import Voluntario, Veterinario
from repositorio import RepositorioCasos
from vista import CasoVista


def main():
    publicador = PublicadorRescates()
    for canal in (NotificadorCorreo(), NotificadorSMS(), PanelVoluntario()):
        publicador.suscribir(canal)

    controlador = CasoControlador(RepositorioCasos(), CasoVista(), publicador)

    c1 = controlador.reportar({"ubicacion": "Av. Principal", "descripcion": "Perro herido",
                               "animal": Perro("Max"), "foto": "perro.jpg"})
    c2 = controlador.reportar({"ubicacion": "Parque Samanes", "descripcion": "Búho caído",
                               "animal": FaunaSilvestre("Búho")})
    controlador.reportar({"ubicacion": "Mercado Sur", "descripcion": "Gata con crías", "animal": Gato("Mía")})

    personal = [Voluntario("Ana"), Veterinario("Dr. Mora", especialidad="fauna silvestre"), Voluntario("Luis")]
    controlador.asignar_encargado(c1, personal, AsignacionPorCarga())
    controlador.asignar_encargado(c2, personal, AsignacionPorEspecialidad())

    controlador.avanzar_caso(c1.id, "Dr. Mora")      # Rescatado -> EnTratamiento
    controlador.avanzar_caso(c1.id, "Dr. Mora")      # sin alta médica: no se permite
    c1.alta_medica = True
    controlador.avanzar_caso(c1.id, "Dr. Mora")      # EnTratamiento -> EnAdopcion

    print("\nCasos del refugio:")
    controlador.consultar()


if __name__ == "__main__":
    main()
