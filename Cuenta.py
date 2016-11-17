class Cuenta:
    def __init__(self, nombre, numero, saldo=200.00):
        self.nombre = nombre
        self.numero= numero
        self.saldo= saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise RuntimeError("Cantidad no disponible")
        self.saldo -= cantidad
        return self.saldo