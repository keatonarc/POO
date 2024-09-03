filename = 'informacion.dat'

nuevo_contenido = (
    "Hola Mundo\n"
    "Este en una nueva línea en el archivo\n"
    "agregando la segunda línea del archivo\n"
    "finalizando la línea agregada\n"
)

with open(filename, 'a') as file:
    file.write(nuevo_contenido)

print(f"El contenido ha sido agregado exitosamente al archivo {filename}.")
