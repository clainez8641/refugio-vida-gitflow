# RefugioVida – Control de Rescate y Adopción Animal

Plataforma para llevar el control de los casos de rescate y adopción de un refugio animal:
recibe reportes, avisa al personal, asigna un encargado y registra cada etapa
(Rescatado → En Tratamiento → En Adopción → Adoptado).

Proyecto de la Actividad 1 – Desarrollo de Sistemas Informáticos (Unidad 1).

## Patrones de diseño
| Patrón | Clases principales | Rama feature |
|---|---|---|
| Observer | `PublicadorRescates`, `Suscriptor` y sus canales | `feature/observer-notificaciones` |
| State | `EstadoCaso`, `Rescatado`, `EnTratamiento`, `EnAdopcion`, `Adoptado` | `feature/state-estados` |
| Strategy | `EstrategiaAsignacion`, `AsignadorEncargado` | `feature/strategy-asignacion` |
| MVC | `CasoControlador`, `CasoVista`, `RepositorioCasos` | `feature/mvc-interfaz` |

## Gitflow
- `master`: versiones estables (etiqueta `v1.0.0`).
- `develop`: integración de funcionalidades terminadas.
- `feature/*`: una rama por funcionalidad, integrada con pull request.

## Ejecutar (Python 3.8 o superior)
```bash
python src/main.py
```

## Documentación
Diagramas UML en `docs/diagramas/`.
