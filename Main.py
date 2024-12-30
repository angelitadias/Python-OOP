class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "8755554444")
conta = Conta(0, c1.telefone,6565)

print(c1)
print(f"{c1.nome} e {c1.telefone}")

print(conta.titular, "Num: ", conta.numero, "Saldo:", conta.saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()