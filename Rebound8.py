import os

filename = 'informacion.dat'

if os.path.exists(filename):
    print(f"El archivo '{filename}' ya existe.")
else:
    with open(filename, 'w') as file:
        file.write("Datos de información en la línea 1\n")
        file.write("Datos de información en la línea 2\n")
        file.write("Datos de información en la línea 3\n")
        file.write("Datos de información en la línea 4\n")
        file.write("Datos de información en la línea 5\n")
    
    print(f"El archivo '{filename}' ha sido creado exitosamente.")
