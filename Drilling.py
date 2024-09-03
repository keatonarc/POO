# Persona
class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} {self.apellidos} se está concentrando.")
    
    def viajar(self):
        print(f"{self.nombre} {self.apellidos} está viajando.")

# Clase Futbolista
class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugar_partido(self):
        print(f"{self.nombre} {self.apellidos} está jugando un partido.")
    
    def entrenar(self):
        print(f"{self.nombre} {self.apellidos} está entrenando.")


# Clase Entrenador
class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion
    
    def dirigir_partido(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo un partido.")
    
    def dirigir_entrenamiento(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo un entrenamiento.")

# Clase Masajista
class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annos_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annos_experiencia = annos_experiencia
    
    def dar_masajes(self):
        print(f"{self.nombre} {self.apellidos} está dando masajes.")

#instancias de las clases

futbolista1 = Futbolista(id=1, nombre="Lionel", apellidos="Messi", edad=36, dorsal=10, demarcacion="Delantero")

entrenador1 = Entrenador(id=2, nombre="Pep", apellidos="Guardiola", edad=53, id_federacion="FED1234")

masajista1 = Masajista(id=3, nombre="Juan", apellidos="Pérez", edad=45, titulacion="Fisioterapeuta", annos_experiencia=20)

#métodos

# Futbolista
futbolista1.concentrarse()  
futbolista1.viajar()        
futbolista1.jugar_partido() 
futbolista1.entrenar()      
# Entrenador
entrenador1.concentrarse()        
entrenador1.viajar()             
entrenador1.dirigir_partido()     
entrenador1.dirigir_entrenamiento() 

# Masajista
masajista1.concentrarse()  
masajista1.viajar()        
masajista1.dar_masajes()   