class CuentaBancaria:
    cuentas=[]
    def __init__ (self,tasa_de_interes,balance):
        self.tasa_de_interes = tasa_de_interes
        self.balance = balance 
        CuentaBancaria.cuentas.append(self)

    def deposito(self,cantidad):
        self.balance += cantidad
        return self
    
    def retiro(self,cantidad):
        if (self.balance-cantidad)<=0:
            print('"Fondos insuficientes: cobrando una tarifa de $5"')
            self.balance-=5
        else:
            self.balance-=cantidad
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if self.balance>0:
            self.balance += (self.balance * self.tasa_de_interes)
        return self

    @classmethod
    def imprimir_todas_instancias(cls):
        for i in cls.cuentas:
            i.mostrar_info_cuenta()

raul=CuentaBancaria(0.03, 200)
nicole=CuentaBancaria(0.02, 600)

raul.deposito(100).deposito(150).deposito(300).retiro(480).generar_interes().mostrar_info_cuenta()
print('---------------------')
nicole.deposito(50).deposito(30).retiro(100).retiro(50).retiro(400).retiro(250).generar_interes().mostrar_info_cuenta()
print('---------------------')

CuentaBancaria.imprimir_todas_instancias()


