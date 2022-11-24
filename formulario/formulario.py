import tkinter
import sqlite3
from tkinter import messagebox
#ventana
ventana=tkinter.Tk()
barraMenu= tkinter.Menu(ventana)
ventana.title("Formulario")
ventana.config(menu=barraMenu, width=300, height=300)


def conexionformulario():
    miconexion=sqlite3.connect("Usuario")
    micursor=miconexion.cursor()

    try:
        micursor.execute(
            '''
            CREATE TABLE USUARIO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_DE_USUARIO VARCHAR (50),
            CONTRASEÑA VARCHAR (20),
            CORREO VARCHAR (30))
            '''
        )
        messagebox.showinfo("Menu", "Base de datos creada con exito!!!")
    except:
        messagebox.showwarning("!Atencion!", "Base de datos ya existe!!!")


def saliraplicacion():
    mensaje=messagebox.askquestion("Salir", "¿Quieres salir de la base de datos")
    if mensaje == "yes":
        ventana.destroy()


def limpiar_campo():
    miId.set("")
    miNombre.set("")
    miContrasena.set("")
    miCorreo.set("")

def insertar():
    miconexion = sqlite3.connect("Usuario")
    micursor = miconexion.cursor()

    insertando=miNombre.get(), miContrasena.get(), miCorreo.get()
    micursor.execute("INSERT INTO USUARIO VALUES(NULL,?,?,?)",(insertando))

    miconexion.commit()
    messagebox.showinfo("base de datos", "Registro insertado con exito!!!!")

def leerdatos():
    miconexion=sqlite3.connect("usuario")
    micursor=miconexion.cursor()

    micursor.execute("SELECT * FROM USUARIO WHERE ID=" + miId.get())

    mileer=micursor.fetchall()
    for leer in mileer:
        miId.set(leer[0])
        miNombre.set(leer[1])
        miContrasena.set(leer[2])
        miCorreo.set(leer[3])

    miconexion.commit()


def actualizar():
    miconexion=sqlite3.connect("usuario")
    micursor=miconexion.cursor()

    insertando=miNombre.get(), miContrasena.get(), miCorreo.get()
    micursor.execute("UPDATE USUARIO SET NOMBRE_USUARIO=?,PASSWORD=?,CORREO=?"+ "WHERE ID="+ miId.get(),(insertando))

    miconexion.commit()
    messagebox.showinfo("base de datos", "Registro actualizado con exito")

def eliminar():
    miconexion=sqlite3.connect("usurio")
    micursor=miconexion.cursor()

    micursor.execute("DELETE FROM USUARIO WHERE ID=" + miId.get())
    miconexion.commit()
    messagebox.showinfo("base de datos", "borrado con exito")


# boton menu
botonMenu1=tkinter.Menu(barraMenu, tearoff=0)
botonMenu1.add_command(label="Conectar", command=conexionformulario)
botonMenu1.add_command(label="Salir", command=saliraplicacion)

#boton borrar
botonMenu2=tkinter.Menu(barraMenu, tearoff=0)
botonMenu2.add_command(label="Borrar")


#funciones de boton
barraMenu.add_cascade(label="Menu", menu=botonMenu1)
barraMenu.add_cascade(label="Borrar", menu=botonMenu2)

# creacion del frame
miframe=tkinter.Frame(ventana)
miframe.pack()

miId=tkinter.StringVar()
miNombre=tkinter.StringVar()
miContrasena=tkinter.StringVar()
miCorreo=tkinter.StringVar()


#boton ID
id=tkinter.Label(miframe, text="ID")
id.grid(row=0, column=1, pady=5, padx=5)
iDespacio=tkinter.Entry(miframe, textvariable=miId)
iDespacio.grid(row=0, column=2, pady=5, padx=5)

#boton nombre
nombre=tkinter.Label(miframe, text="NOMBRE")
nombre.grid(row=2, column=1, pady=5, padx=5)
nombreEspacio=tkinter.Entry(miframe, textvariable=miNombre)
nombreEspacio.grid(row=2, column=2, pady=5, padx=5)

#boton contraseña
contrasena=tkinter.Label(miframe, text="CONTRASEÑA")
contrasena.grid(row=4, column=1, pady=5, padx=5)
contrasenaEspacio=tkinter.Entry(miframe, textvariable=miContrasena)
contrasenaEspacio.grid(row=4, column=2, pady=5, padx=5)
contrasenaEspacio.config(show="*")

#boton correo
correo=tkinter.Label(miframe, text="CORREO")
correo.grid(row=6, column=1, pady=5, padx=5)
correoEspacio=tkinter.Entry(miframe, textvariable=miCorreo)
correoEspacio.grid(row=6, column=2, pady=5, padx=5)

#creacion de frame 2
miframe2=tkinter.Frame(ventana)
miframe2.pack()

#boton crear
botonCrear=tkinter.Button(miframe2, text="Crear", command=insertar)
botonCrear.grid(row=0, column=0, padx=5, pady=5)

#boton actualizar
botonActualizar=tkinter.Button(miframe2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=1, padx=5, pady=5)

#boton Leer
botonLeer=tkinter.Button(miframe2, text="Leer", command=leerdatos)
botonLeer.grid(row=0, column=2, padx=5, pady=5)

#boton Borrar
botonBorrar=tkinter.Button(miframe2, text="Borrar", command=limpiar_campo)
botonBorrar.grid(row=0, column=3, padx=5, pady=5)

#boton Eliminar
botonEliminar=tkinter.Button(miframe2, text="Eliminar", command=eliminar)
botonEliminar.grid(row=0, column=4, padx=5, pady=5)

tkinter.mainloop()