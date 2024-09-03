#rebound 7
while True:
    try:
        # Pedimos la edad al usuario
        edad = int(input("Por favor, ingrese su edad: "))
        # Verificamos si el usuario es adulto o no
        if edad >= 18:
            print("Es Adulto.")
        else:
            print("No es un Adulto.")
        break  # Salimos del bucle después de procesar una entrada válida
    except ValueError:
        # Manejo del caso en que el usuario no ingresa un número entero
        print("Entrada inválida. Por favor, ingrese un número entero.")
