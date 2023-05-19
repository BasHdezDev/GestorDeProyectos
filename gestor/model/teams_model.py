class Equipo:
    def __init__(self, nombre: str, id: str, descripcion: str):
        self.nombre: str = nombre
        self.id: str = id
        self.descripcion: str = descripcion
        self.miembros = []

