import os

def leer_archivo(filename):
    if os.path.exists(filename):
        print(f"El archivo {filename} ya existe, ha sido creado previamente")
                
        with open(filename, 'r') as file:
            contenido = file.read()
        print(contenido)
    else:
        print(f"El archivo {filename} no existe.")

filename = 'informacion.dat'

leer_archivo(filename)
