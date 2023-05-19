import json


def crear_tarea(nombre, id, descripcion):
    tareas = {"nombre": "",
                "id": "",
                "descripcion": ""}

    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\tareas.json", "r",
              encoding="utf-8") as archivo:
        datos = json.load(archivo)

        for tarea in datos:
            if tarea["numero_id"] == id:
                raise Exception

        tareas["nombre"] = nombre
        tareas["numero_id"] = id
        tareas["descripcion"] = descripcion
        datos.append(tareas)

    with open(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\gestor\resources\tareas.json", "w",
              encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=1)

