class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self._nombre = nombre
        self._apellidos = apellidos
        self._sexo = sexo
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellidos(self, apellidos):
        self._apellidos = apellidos

    def set_sexo(self, sexo):
        self._sexo = sexo

    def set_edad(self, edad):
        self._edad = edad

    def set_estatura(self, estatura):
        self._estatura = estatura

    def set_peso(self, peso):
        self._peso = peso

    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_sexo(self):
        return self._sexo

    def get_edad(self):
        return self._edad

    def get_estatura(self):
        return self._estatura

    def get_peso(self):
        return self._peso

    def mostrar_datos(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Apellidos: {self.get_apellidos()}")
        print(f"Sexo: {self.get_sexo()}")
        print(f"Edad: {self.get_edad()} años")
        print(f"Estatura: {self.get_estatura()} mts")
        print(f"Peso: {self.get_peso()} Kg")
        print()

persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.80, 75)

print("Datos iniciales:")
persona_1.mostrar_datos()
persona_2.mostrar_datos()

persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")

print("Datos actualizados:")
persona_1.mostrar_datos()
persona_2.mostrar_datos()
