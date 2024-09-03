import csv

class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def mostrar_info(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

    def guardar_datos_csv(self):
        class_name = self.__class__.__name__
        attributes = {k: v for k, v in self.__dict__.items()}
        with open('vehiculos.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([f"<class '__main__.{class_name}'>", str(attributes)])

    @staticmethod
    def leer_datos_csv():
        vehiculos = {
            'Particular': [],
            'Carga': [],
            'Bicicleta': [],
            'Motocicleta': []
        }
        try:
            with open('vehiculos.csv', 'r') as archivo:
                reader = csv.reader(archivo)
                seen = set()  # Para evitar duplicados
                for row in reader:
                    if len(row) < 2:
                        continue
                    class_name = row[0].split('.')[-1].split('\'')[0]
                    attributes = eval(row[1])
                    if class_name in vehiculos:
                        attributes_tuple = tuple(attributes.items())
                        if attributes_tuple not in seen:
                            vehiculos[class_name].append(attributes)
                            seen.add(attributes_tuple)

            for tipo, lista in vehiculos.items():
                if lista:
                    print(f"Lista de Vehiculos {tipo}")
                    for atributos in lista:
                        print(atributos)
        except FileNotFoundError:
            print("El archivo vehiculos.csv no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_info(self):
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, "
                f"{self.velocidad} Km/h, {self.cilindrada} cc")

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def mostrar_info(self):
        return (f"{super().mostrar_info()}, Puestos: {self.nro_puestos}")

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def mostrar_info(self):
        return (f"{super().mostrar_info()}, Carga: {self.carga} Kg")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def mostrar_info(self):
        return (f"{super().mostrar_info()}, Motor: {self.motor}, Cuadro: {self.cuadro}, "
                f"Nro Radios: {self.nro_radios}")
