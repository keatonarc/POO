class Persona:
    def __init__(self, numero_identificacion, nombre, apellido):
        self.numero_identificacion = numero_identificacion
        self.nombre = nombre
        self.apellido = apellido

    def obtener_datos(self):
        return f"ID: {self.numero_identificacion}, Nombre: {self.nombre}, Apellido: {self.apellido}"

class Estudiante(Persona):
    def __init__(self, numero_identificacion, nombre, apellido, codigo_alumno, matricula):
        super().__init__(numero_identificacion, nombre, apellido)
        self.codigo_alumno = codigo_alumno
        self.matricula = matricula

    def obtener_datos(self):
        datos_persona = super().obtener_datos()
        return f"{datos_persona}, Codigo Alumno: {self.codigo_alumno}, Matricula: {self.matricula}"

persona = Persona("12345678", "Juan", "Perez")
estudiante = Estudiante("87654321", "Ana", "Gomez", "A123", "2024001")

print(persona.obtener_datos())  
print(estudiante.obtener_datos())  