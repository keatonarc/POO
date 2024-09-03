class Persona:
    def __init__(self, nombre, apellido, año):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = año

class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, año, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, año)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario

trabajador = Trabajador(
    nombre="Juan",
    apellido="Perez",
    año=2005,
    nombre_dpto="Ingenieria de software",
    nombre_corto_dpto="IS",
    salario=20000
)

print(trabajador.__dict__)

print(isinstance(trabajador, Persona))         
print(isinstance(trabajador, Departamento))    
print(isinstance(trabajador, Trabajador))      