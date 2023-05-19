import json


def registrar_equipo(nombre, equipo_id, descripcion):
    equipo = {"id_equipo": "", "miembros": [], "nombre": "", "descripcion": "", "Tarea": ""}

    with open(r'C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json', "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

        equipo["nombre"] = nombre
        equipo["id_equipo"] = equipo_id
        equipo["descripcion"] = descripcion

        datos.append(equipo)

    with open(r'C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json', "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)


def asignar_usuario(nombre, id_a_asignar):
    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

        for linea in datos:
            if linea["nombre"] == nombre:
                linea["miembros"].append(id_a_asignar)

    with open(r'C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json', "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)


def asignar_tarea(equipo, tarea):
    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

        for linea in datos:
            if linea["nombre"] == equipo:
                linea["Tarea"] = tarea

    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\equipos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)


asignar_tarea("1", "Dormir")


