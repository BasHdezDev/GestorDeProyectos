
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, messagebox, Button, PhotoImage

from view.pages.home_page.build.gui import ejecutar_script

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Bas\PycharmProjects\GestorDeProyectos\view\pages\team_page\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("716x427")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 427,
    width = 716,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    358.0,
    213.0,
    image=image_image_1
)

canvas.create_rectangle(
    7.0,
    383.0,
    155.0,
    427.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    67.0,
    404.0,
    image=image_image_2
)

canvas.create_rectangle(
    416.0,
    80.0,
    878.0,
    312.0,
    fill="#35B347",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    332.0,
    367.0,
    fill="#35B347",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    572.0,
    196.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=481.0,
    y=179.0,
    width=182.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    165.5,
    101.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=35.0,
    y=84.0,
    width=261.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    165.5,
    241.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=35.0,
    y=213.0,
    width=261.0,
    height=54.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    165.5,
    165.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=35.0,
    y=148.0,
    width=261.0,
    height=32.0
)

canvas.create_text(
    60.0,
    15.0,
    anchor="nw",
    text="Crea un equipo",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 30 * -1)
)

canvas.create_text(
    444.0,
    101.0,
    anchor="nw",
    text="Únete a un equipo",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 30 * -1)
)

canvas.create_text(
    466.0,
    157.0,
    anchor="nw",
    text="Id del equipo:",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 16 * -1)
)

canvas.create_text(
    29.0,
    62.0,
    anchor="nw",
    text="Nombre del equipo:",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 16 * -1)
)

canvas.create_text(
    29.0,
    131.0,
    anchor="nw",
    text="Id del equipo:",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 16 * -1)
)

canvas.create_text(
    29.0,
    196.0,
    anchor="nw",
    text="Descripción:",
    fill="#FFFFFF",
    font=("Inconsolata ExtraBold", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: messagebox.showinfo(message="Equipo creado!", title="Proceso Exitoso"),
    relief="flat"
)
button_1.place(
    x=90.0,
    y=307.0,
    width=150.0,
    height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: messagebox.showinfo(message="Te has unido satisfactoriamente", title="Proceso exitoso"),
    relief="flat"
)
button_2.place(
    x=497.0,
    y=235.0,
    width=150.0,
    height=34.0
)
window.resizable(False, False)
window.mainloop()
