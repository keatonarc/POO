class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        self._peso = peso

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_raza(self, raza):
        self._raza = raza

    def set_edad(self, edad):
        self._edad = edad

    def set_peso(self, peso):
        self._peso = peso

    def get_nombre(self):
        return self._nombre

    def get_raza(self):
        return self._raza

    def get_edad(self):
        return self._edad

    def get_peso(self):
        return self._peso

    def mostrar_datos(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Raza: {self.get_raza()}")
        print(f"Edad: {self.get_edad()} años")
        print(f"Peso: {self.get_peso()} kg")
        print()

caballo = Animal("Zeus", "Pura sangre", 5, 450)
leon = Animal("Boulder", "Atlas", 10, 130)

print("Datos del caballo:")
caballo.mostrar_datos()

print("Datos del león:")
leon.mostrar_datos()
