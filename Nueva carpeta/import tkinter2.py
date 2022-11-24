import tkinter 

ventana=tkinter.Tk()
ventana.geometry("500x500")
ventana.title("mi primera ventana")

etiqueta=tkinter.Label(ventana, text="Mi primera ventana")
etiqueta.grid()

boton1=tkinter.Button(ventana, text="boton1")
boton2=tkinter.Button(ventana, text="boton2")
boton3=tkinter.Button(ventana, text="boton3")
boton4=tkinter.Button(ventana, text="boton4")
boton5=tkinter.Button(ventana, text="boton5")

boton1.grid(row=1 , column=0)
boton2.grid(row=1 , column=1)
boton3.grid(row=1 , column=2)
boton4.grid(row=1 , column=3)
boton5.grid(row=1 , column=4)

def Texto():
    texto= cajatexto.get()
    print(texto)

cajatexto=tkinter.Entry()
cajatexto.grid()

boton1=tkinter.Button(ventana, text="presionar", padx="5", pady="5" ,command=Texto)
boton1.grid()



tkinter.mainloop()
