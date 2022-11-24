class vehiculo:
    def __init__(self, nombre, marca, modelo, color) -> None:
        pass
        self.nombre=nombre
        self.marca=marca
        self.modelo=modelo
        self.color=color
    
    def descripcion (self):
        print ("\nNombre: ",self.nombre, "\nMarca: ",self.marca, "\nModelo: ",self.modelo, "\nColor: ",self.color)



class carro(vehiculo):
    pass
vehiculo_uno=carro("carro","Nissan","2020","Negro")

vehiculo_uno.descripcion()

class Moto(vehiculo):
    pass

moto_uno=vehiculo("Moto","yamaha","2020","azul")
moto_uno.descripcion()



class cicla(vehiculo):
    pass
    def movimiento(self,andando):

        self.andando=andando

        if(self.andando==True):
            return "la cicla va subiendo la montaña"
        else:
            return "la cicla esta parada"

    def Llanta(self):
        self.llanta_Waldo="la cicla tiene 2 llantas"

        print(self.llanta_Waldo)
    
cicla_uno=cicla("Cicla","MTB","2021","Gris")

cicla_uno.descripcion()

print(cicla_uno.movimiento(andando=""))

print(cicla_uno.Llanta())
