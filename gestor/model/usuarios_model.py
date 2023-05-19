class Usuario:
    def __init__(self, nombre: str, numero_id: str, contrasena: str, email: str,  cargo: str):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.email: str = email
        self.cargo: str = cargo

