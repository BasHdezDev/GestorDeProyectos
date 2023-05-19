import json


def registrar_equipo(self):
    equipos = {"nombre": "",
               "id": "",
               "contrasena": "",
               "email": "",
               "cargo": ""}

    with open("equipos.json", "r", encoding="utf-8") as archivo:
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