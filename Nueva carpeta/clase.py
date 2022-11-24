class jugador:
    def __init__(self, nombre, ataque, resistencia, regateo):
        pass
        self.nombre=nombre
        self.ataque=ataque
        self.resistencia=resistencia
        self.regateo=regateo


jugador_uno=jugador("messi",50,80,90)
jugador_dos=jugador("cristiano",100,100,90)
jugador_tres=jugador("Diaz",80,90,90)

print("nombre del jugador",jugador_uno.nombre,"su habilidad es", jugador_dos.ataque)

