class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        return f"{self.nombre} esta comiendo."

    def caminar(self):
        return f"{self.nombre} esta caminando."

    def dormir(self):
        return f"{self.nombre} esta durmiendo."

    def __str__(self):
        return (f"Nombre: {self.nombre}, Raza: {self.raza}, "
                f"Edad: {self.edad} años, Peso: {self.peso} kg")

class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, raza, edad, peso)

class Gato(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, raza, edad, peso)
        
brando = Perro(nombre="Brando", edad=3, raza="San Bernardo", peso=30)
roll = Gato(nombre="Roll", edad=4, raza="Persa", peso=3)

print(brando)
print(brando.comer())
print(brando.caminar())
print(brando.dormir())

print(roll)
print(roll.comer())
print(roll.caminar())
print(roll.dormir())