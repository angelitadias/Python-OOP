
from Cliente import Cliente

class Conta:
    def __init__(self, saldo, numero, titular):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    def get_saldo(self):
        return self._saldo

    def set_nome(self, saldo):
        if (saldo<0):
            print("o saldo não pode ser negativo.")

        else:
            self._saldo = saldo

    def saque(self, valor):
        if(self.saldo>=valor):
            self.saldo-=valor
            print("saque realizadp!")
        else:
            print("saldo insuficiente.")

    def deposita(self,valor):
        self.saldo+=valor

    def extrato(self):
    print(f"cliente: {self._titular} saldo: {self._saldo}")