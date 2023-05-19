class Tarea:
    def __init__(self, nombre: str, id: int, descripcion: str, fecha_inicial: int, fecha_limite: int, prioridad: str, desarrollo: int):
        self.nombre: str = nombre
        self.id: int = id
        self.descripcion: str = descripcion
        self.fecha_inicial: int = fecha_inicial
        self.fecha_limite: int = fecha_limite
        self.prioridad: str = prioridad
        self.desarrollo: int = desarrollo
        estado: bool = False

