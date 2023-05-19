from gestor.model.tareas_model import crear_tarea
from gestor.model.teams_model import Equipo, registrar_equipo, asignar_usuario
from gestor.model.usuarios_model import Usuario, iniciar_sesion, registrar_usuario, buscar_usuario


while True:
    decision = input("\n\n1) Registrar usuario\n2) Iniciar sesion\n3) Buscar un usuario\n4)Crear un equipo\n"
                     "5) Asignar un usuario a un equipo\n6) Crear tarea\n7) Asignar tarea a un equipo\n\n")

    if decision == "1":
        nombre = input("Ingrese el nombre: ")
        numero_id = input("Ingrese el id: ")
        contrasena = input("Ingrese la contrasena: ")
        correo = input("Ingrese el correo: ")
        cargo = input("Ingrese el cargo: ")
        registrar_usuario(numero_id, contrasena, correo, cargo)

    elif decision == "2":
        id = input("Ingrese su id: ")
        contrasena = input("Ingrese la contraseña: ")
        iniciar_sesion(id, contrasena)

    elif decision == "3":
        id = input("Ingrese un id para buscarlo: ")
        if buscar_usuario(id):
            print("El usuario ya existe: ")
        else:
            nombre = input("Ingrese el nombre: ")
            numero_id = input("Ingrese el id: ")
            contrasena = input("Ingrese la contrasena: ")
            correo = input("Ingrese el correo: ")
            cargo = input("Ingrese el cargo: ")
            registrar_usuario(nombre, numero_id, contrasena, correo, cargo)
    elif decision == "4":
        nombre = input("Ingrese el nombre del equipo: ")
        id = input("Ingrese el id del equipo: ")
        descripcion = input("Ingrese una descripcion del equipo: ")
        registrar_equipo(nombre, id, descripcion)
    elif decision == "5":
        nombre = input("Ingrese el nombre del equipo al cual quiere asignarle un usuario: ")
        id = input("Ingrese el id del usuario a asignar: ")
        asignar_usuario(nombre, id)
    elif decision == "6":
        nombre = input("Ingrese el nombre de la tarea: ")
        id = input("Ingrese el id de la tarea: ")
        descripcion = input("Ingrese una descripción de la tarea: ")
        crear_tarea(nombre, id, descripcion)
    elif decision == "7":
        equipo = input("Ingrese el nombre del equipo al cual le va a asignar la tarea: ")
        tarea = input("Ingrese la tarea a asignar: ")

