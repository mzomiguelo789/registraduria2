from tkinter import *


ventana=tkinter.Tk()
ventana.geometry("300x300")
ventana.title("mi primera ventana")

etiqueta=tkinter.Label(ventana, text="Mi primera")
etiqueta.pack()

#def saludo():

    #print("mi primer hola mundo")

def Texto():
    texto= cajatexto.get()
    print(texto)

cajatexto=tkinter.Entry()
cajatexto.pack()

boton_uno=tkinter.Button(ventana, text="presionar", padx="5", pady="5" ,command=Texto)
boton_uno.pack()

tkinter.mainloop()


