from dataclasses import dataclass


@dataclass
class Usuario:
    nombre: str
    id: int
    email: str
    cargo: str

    def buscar_id(self) -> bool:
        pass

    def agregar_id(self) -> bool:
        pass

@dataclass
class Equipo:
    nombre: str
    id: int
    descripcion: str
    miembros: int

    def asignar_usuario(self) -> bool:
        pass

    def asignar_tarea(self) -> bool:
        pass

    def unirse(self) -> bool:
        pass


@dataclass
class Tarea:
    nombre: str
    id: int
    descripcion: str
    fecha_inicial: int
    fecha_limite: int
    prioridad: str
    desarrollo: int
    estado: bool = False

    def editar_tarea(self) -> bool:
        pass

    def recordatorio(self) -> bool:
        pass