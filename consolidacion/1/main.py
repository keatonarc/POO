from Automovil import Vehiculo, Particular, Carga, Bicicleta, Motocicleta

def main():
    # Crear instancias de los vehículos
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Guardar datos en el archivo CSV
    particular.guardar_datos_csv()
    carga.guardar_datos_csv()
    bicicleta.guardar_datos_csv()
    motocicleta.guardar_datos_csv()

    # Leer datos del archivo CSV y mostrar información
    Vehiculo.leer_datos_csv()

if __name__ == "__main__":
    main()
