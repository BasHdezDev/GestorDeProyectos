import json


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
