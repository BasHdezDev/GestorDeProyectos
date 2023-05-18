import tkinter

import tkdesigner

ventana = tkinter.Tk()
ventana.geometry("600x600")


fondo = tkinter.Label(ventana, bg="#FFFCE8")
etiqueta = tkinter.Label(ventana, text="Bienvenido a mi aplicación", bg="#FFFCE8")
boton_registrar_usuario = tkinter.Button(fondo, text="Registrar usuario", padx=20, pady=10)

boton_registrar_equipo = tkinter.Button(fondo, text="Registrar equipo", padx=20, pady=10)

etiqueta.pack(side=tkinter.TOP, fill=tkinter.X)
fondo.pack(fill=tkinter.BOTH, expand=1)
boton_registrar_usuario.grid(row=0, column=0)
boton_registrar_equipo.grid(row=0, column=2)


ventana.mainloop()