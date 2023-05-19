import json
from pathlib import Path


def iniciar_sesion(numero_id, contrasena):

    data_folder = Path(r"..resources")
    file_to_open = data_folder / r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\usuarios.json"

    with open(file_to_open, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for linea in datos:
            if linea["numero_id"] == numero_id and linea["contrasena"] == contrasena:
                print("Inicio de sesión exitoso")
                return

        print("El usuario o contraseña no coinciden")


def buscar_usuario(numero_id: str):

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


def registrar_usuario(nombre, numero_id, contrasena, email, cargo):

    usuarios = {"nombre": "",
                "numero_id": "",
                "contrasena": "",
                "email": "",
                "cargo": ""}

    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\usuarios.json", "r",
              encoding="utf-8") as archivo:
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

    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\usuarios.json", "w",
              encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)


class Usuario:
    def __init__(self, nombre: str, numero_id: str, contrasena: str, email: str,  cargo: str):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.email: str = email
        self.cargo: str = cargo
