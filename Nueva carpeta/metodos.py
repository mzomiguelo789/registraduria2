"""class Ropa:
    def __init__(self):
        self.marca = "polo"
        self.talla = "S"
        self.color = "negro"
        

camisa = Ropa()
jean = Ropa()"""


class Ropa:
    def __init__(self, marca, color, talla):
        pass
        self.marca = marca
        self.color = color
        self.talla = talla

    def descripcion(self):
        print("marca: ", self.marca, "color: ", self.color, "talla: ", self.talla)


class Camisa(Ropa):
    pass


camisaUna = Camisa("Polo", "Negro", "S")
camisaUna.descripcion()
