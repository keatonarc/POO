class Cliente:
    def __init__(self, nombre, direccion, numero_identificacion):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_identificacion = numero_identificacion

    def obtener_datos(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, ID: {self.numero_identificacion}"

class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto

    def consultar_saldo(self):
        return self.saldo

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo):
        super().__init__(numero_cuenta, titular, saldo)
        self.cantidad_retiros = 0

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto
        self.cantidad_retiros += 1

class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo, limite_credito):
        super().__init__(numero_cuenta, titular, saldo)
        self.limite_credito = limite_credito

    def retirar(self, monto):
        if monto > (self.saldo + self.limite_credito):
            raise ValueError("Límite de crédito excedido")
        self.saldo -= monto

class Banco:
    def __init__(self, nombre, codigo_banco, direccion):
        self.nombre = nombre
        self.codigo_banco = codigo_banco
        self.direccion = direccion

    def realizar_transferencia(self, cuenta_origen, cuenta_destino, monto):
        cuenta_origen.retirar(monto)
        cuenta_destino.depositar(monto)

cliente1 = Cliente("Ana Pérez", "Calle Falsa 123", "ID001")
cliente2 = Cliente("Luis Gómez", "Avenida Siempre Viva 456", "ID002")

cuenta_ahorro = CuentaAhorro("0001", cliente1, 1000)
cuenta_corriente = CuentaCorriente("0002", cliente2, 500, 200)

banco = Banco("Banco Ejemplo", "BE001", "Calle Principal 789")

banco.realizar_transferencia(cuenta_ahorro, cuenta_corriente, 100)

print(f"Saldo Cuenta Ahorro: {cuenta_ahorro.consultar_saldo()}") 
print(f"Saldo Cuenta Corriente: {cuenta_corriente.consultar_saldo()}")  