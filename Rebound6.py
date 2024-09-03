#ejercicio rebound 6
suma = 3000
contador = 0
#clausula try...except (zerodivisionerror)
try:
    resultado = suma / contador
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Division es por cero.")
