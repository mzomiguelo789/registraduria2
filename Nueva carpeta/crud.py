
class contacto:
    pass
    def __init__(self,nombre,apellido,telefono,correo) -> None:
        pass
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.correo=correo
    def __str__(self) -> str:
        pass
        return f"nombre= {self.nombre},apellido= {self.apellido},telefono={self.telefono},correo={self.correo}"
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def setNombre(self, pnombre):
        self.nombre=pnombre
    def setApellido(self, papellido):
        self.apellido=papellido
    def setTelefono(self, ptelefono):
        self.ptelefono=ptelefono
    def setCorreo(self, pcorreo):
        self.pcorreo=pcorreo
def agregarUsu():
    nombre=input("ingresar nombre :")
    apellido=input("ingresar apellido :")
    telefono=input("ingresar telefono :")
    correo=input("ingresar correo :")
    contacto1 = contacto(nombre,apellido,telefono,correo)
    listaccontacto.append(contacto1)
    #print(contacto1)

def informecontacto():

    print("\n--------------------\n")
    for indice in range(0,len(listaccontacto)):
        print(f"{indice+1} - ")
    print("\n--------------------reporte contacto-----------------------\n")

def borrarcontacto():
    print("\n----\n")
    for conta in listaccontacto:
        print ()

def borrarcontacto():

    informecontacto()

    indice= int (input ("ingrese el numero de la persona que quiere borrar:"))
    #print (f"esta seguro de eliminar el contacto {listaccontacto{indice -1].getApellido()) (listaccontact
    repuesta= input(" si para borrar o no para no borar : ")
    if (repuesta=="si"):
        listaccontacto.remove(listaccontacto[indice-1])
def modificarcontacto():
    informecontacto()
    indice=int (input ("ingrese el numero del contacto a modificar:'"))
    nombre=input ("ingrese nuevo nombre:")
    listaccontacto[indice -1].setNombre(nombre)
    apellido=input("ingrese nuevo apellido:")
    telefono=input("ingrese nuevo telefono:")
    correo=input ("ingrese nuevo correo:")
listaccontacto = []
opcion = ""
while (opcion != "x"):

    print("***Menu de contacto*******")
    print("precione las siguientes letras")
    print("\na.. para agregar contacto")
    print("m.. para modificar contacto")
    print("i.. para informe de contactos")
    print("b.. para borrar contacto")
    print("x.. para salir")
    opcion=input("ingrese la opcion deseada:")


    if (opcion=="x"):

        print("\nsaliendo del programa......")

    elif (opcion=="a"):

        agregarUsu()
    
    elif (opcion=="i"):
    
        informecontacto()
    #else:
        #print("xxxx")
    elif(opcion=="b"):
        borrarcontacto()
    elif(opcion=="m"):
        modificarcontacto()






   




  

    
 

    


    
