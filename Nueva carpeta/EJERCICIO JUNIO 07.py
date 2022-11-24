class peliculas:
    def __init__(self, nombre, protagonista, duracion, genero) -> None:
        pass
        self.nombre=nombre
        self.protagonista=protagonista
        self.duracion=duracion
        self.genero=genero
    def descripcion (self):
        print ("\nnombre: ", self.nombre, "\nprotagonista: ", self.protagonista, "\nduracion: ", self.duracion, "\ngenero: ", self.genero)

class pelicula(peliculas):
    pass
pelicula_uno=pelicula("Juicio", "Johnny Depp", "90 minutos", "Drama")

pelicula_uno.descripcion()

Pelicula_dos=pelicula("La momia", "Arnold Vosloo", "120 minutos", "Accion y aventura")

Pelicula_dos.descripcion()

pelicula_tres=pelicula("La momia regresa", "Brendan Fraser", "120 minutos", "Accion y aventura")

pelicula_tres.descripcion()

class pelicula(peliculas):
    pass
    def disponibilidad(self,alquiler):
        self.alquiler=alquiler

        if(self.alquiler==True):
            return "la pelicula se encuentra disponible"
        else:
            return "la pelicula no esta disponible"

pelicula_cuatro=pelicula("La momia 3", "Jet Li", "120 minutos", "Accion y aventura")
pelicula_cuatro.descripcion()

print(pelicula_cuatro.disponibilidad(alquiler=""))













