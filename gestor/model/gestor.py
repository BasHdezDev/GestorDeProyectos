import json


def iniciar_sesion(numero_id, contrasena):
    with open("usuarios.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for linea in datos:
            if linea["numero_id"] == numero_id and linea["contrasena"] == contrasena:
                print("Inicio de sesión exitoso")
                return  # Si encuentra una coincidencia, termina la función aquí
        # Si llega hasta aquí, significa que no encontró ninguna coincidencia
        print("El usuario o contraseña no coinciden")


def registrar_usuario(nombre, numero_id, contrasena, email, cargo):

    usuarios = {"nombre": "",
                "numero_id": "",
                "contrasena": "",
                "email": "",
                "cargo": ""}

    with open("usuarios.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

        for usuario in datos:
            if usuario["numero_id"] == numero_id:
                raise Exception

        usuarios["nombre"] = nombre
        usuarios["numero_id"] = numero_id
        usuarios["contrasena"] = contrasena
        usuarios["email"] = email
        usuarios["cargo"] = cargo
        datos.append(usuarios)

    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)


def buscar_usuario(numero_id: str) -> bool:
        try:
            with open("usuarios.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                for usuario in datos:
                    if usuario["numero_id"] == numero_id:
                        return True

            return False
        except FileNotFoundError:
            print("El archivo usuarios.json no se encontró.")
        except Exception as e:
            print(f"Error no esperado: {str(e)}")


class Usuario:
    def __init__(self, nombre: str, numero_id: str, contrasena: str, email: str,  cargo: str):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.email: str = email
        self.cargo: str = cargo


class Equipo:
    def __init__(self, nombre: str, id: str, descripcion: str):
        self.nombre: str = nombre
        self.id: str = id
        self.descripcion: str = descripcion
        self.miembros = []


    def registrar_equipo(self):
        equipos = {"nombre": "",
                    "id": "",
                    "contrasena": "",
                    "email": "",
                    "cargo": ""}

        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for equipo in datos:
                if equipo["id"] == self.id:
                    raise Exception

            equipos["nombre"] = self.nombre
            equipos["id"] = self.id
            equipos["descripcion"] = self.descripcion
            equipos["miembros"] = self.miembros
            datos.append(equipos)

        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)


    def asignar_usuario(self, id):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for usuario in datos:
                if usuario["numero_id"] == id:
                    self.miembros.append(usuario["numero_id"])
                else:
                    print("El usuario ya pertenece a un equipo o no existe el id")




    def asignar_tarea(self) -> bool:
        pass

    def unirse(self) -> bool:
        pass


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

    def editar_tarea(self) -> bool:
        pass

    def recordatorio(self) -> bool:
        pass



x = Usuario("Jameson", "152", "brainmaster", "bahsbahd@gmail.com", "TechLead")

while True:
    decision = input("1) registrar usuario 2) Iniciar s 3)B 4)Crear equipo")
    if decision == "1":
        nombre = input("Ingrese el nombre")
        numero_id = input("Ingrese el id")
        contrasena = input("Ingrese la contrasena")
        correo = input("Ingrese el correo")
        cargo = input("Ingrese el cargo")
        registrar_usuario(nombre, numero_id, contrasena, correo, cargo)

    elif decision == "2":
        id = input("Ingrese su id ")
        contrasena = input("Ingrese la contraseña ")
        iniciar_sesion(id, contrasena)
         
    elif decision == "3":
        id = input("Ingrese un id pa buscarlo pa ")
        if buscar_usuario(id):
            print("El usuario ya existe ")
        else:
            nombre = input("Ingrese el nombre ")
            numero_id = input("Ingrese el id ")
            contrasena = input("Ingrese la contrasena ")
            correo = input("Ingrese el correo ")
            cargo = input("Ingrese el cargo ")
            registrar_usuario(nombre, numero_id, contrasena, correo, cargo)
    elif decision == "4":
        nombre = input("Ingrese el nombre del equipo ")
        id = input("Ingrese el id del equipo ")
        descripcion = input("Ingrese una descripcion del equipo ")

        Equipo.registrar_equipo(Equipo(nombre, id, descripcion))










