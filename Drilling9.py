def reemplazar_contenido(filename, busqueda, reemplazo):
    with open(filename, 'r') as file:
        contenido = file.read()
    reemplazos = contenido.count(busqueda)
    nuevo_contenido = contenido.replace(busqueda, reemplazo)
    
    with open(filename, 'w') as file:
        file.write(nuevo_contenido)
    print(f"Se realizaron: {reemplazos} remplazos")
    
    print("\nEl contenido del archivo {} es:".format(filename))
    print(nuevo_contenido)

filename = 'informacion.dat'

reemplazar_contenido(filename, "Datos de información", "Datos de Procesamiento")
