#drilling 7
# Definimos la clase de excepción personalizada
class SalarioFueraDeRango(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Función para solicitar y validar el salario
def pedir_salario():
    while True:
        try:
            # Pedimos el valor del salario al usuario
            salario = float(input("Ingrese el valor de su salario: "))
            
            # Verificamos si el salario está en el rango permitido
            if 1000 <= salario <= 2000:
                print(f"Salario aceptado: {salario}")
                break  # Salimos del bucle si el salario es válido
            else:
                # Lanzamos la excepción si el salario no está en el rango
                raise SalarioFueraDeRango("El salario no se encuentra en el rango de 1000 a 2000.")
        
        except ValueError:
            # Manejo de entradas no numéricas
            print("Entrada inválida. Por favor, ingrese un número válido.")
        
        except SalarioFueraDeRango as e:
            # Manejo de la excepción personalizada
            print(e)

# Llamamos a la función para ejecutar el programa
pedir_salario()
