class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def movimiento(self):
        return "caminando"

class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        return "trotando"

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        return "rodando"

persona = Persona("Juan")
maratonista = Maratonista("Ana")
ciclista = Ciclista("Luis")

print(f"{persona.nombre} esta {persona.movimiento()}.") 
print(f"{maratonista.nombre} esta {maratonista.movimiento()}.") 
print(f"{ciclista.nombre} esta {ciclista.movimiento()}.") 