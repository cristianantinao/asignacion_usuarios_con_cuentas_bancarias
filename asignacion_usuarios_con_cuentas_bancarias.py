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
        return f"Balance: ${self.balance}"

    def generar_interes(self):
        if self.balance>0:
            self.balance += (self.balance * self.tasa_de_interes)
        return self

    @classmethod
    def imprimir_todas_instancias(cls):
        for i in cls.cuentas:
            i.mostrar_info_cuenta()

class Usuario:   
    def __init__(self,nombre,email):
        self.nombre= nombre
        self.email= email
        self.cuenta= { "ahorros":CuentaBancaria(0.02,0), "pension": CuentaBancaria(0.05,1000)}

    def mostrar_balance_usuario(self):
        print(f"Usuario:{self.nombre} Ahorros {self.cuenta['ahorros'].mostrar_info_cuenta()}")
        print(f"Usuario:{self.nombre} Pension {self.cuenta['pension'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self,cantidad,usuario): 
        self.cuenta -= cantidad
        usuario.cuenta += cantidad
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()

raul= Usuario('Raul','raul.dojo@coding.com')
raul.cuenta["pension"].deposito(2000)
raul.cuenta["ahorros"].deposito(3990)
raul.mostrar_balance_usuario()