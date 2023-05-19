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
                # Si encuentra una coincidencia, termina la función aquí
        # Si llega hasta aquí, significa que no encontró ninguna coincidencia
        print("El usuario o contraseña no coinciden")

