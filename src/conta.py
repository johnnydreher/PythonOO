"""
Enunciado:
Implemente um sistema simples de contas bancárias com dois tipos de conta.

O sistema deve conter:
- Classe base Conta com:
  - Saldo inicial
  - Métodos depositar(valor) e sacar(valor)
- Classe derivada ContaCorrente:
  - Ao sacar, cobra uma taxa de R$0,50.
- Classe derivada ContaPoupanca:
  - Possui método aplicar_rendimento() que aumenta o saldo em 1%.

O que será avaliado:
- Uso de herança.
- Correção nos cálculos de saque e rendimento.
- Encapsulamento e boas práticas de POO.
"""
# TODO: implementar classes Conta, ContaCorrente e ContaPoupanca
class Conta:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    def get_saldo(self):
        return self.saldo
class ContaCorrente(Conta):
    TAXA_SAQUE = 0.50

    def sacar(self, valor):
        valor_com_taxa = valor + self.TAXA_SAQUE
        return super().sacar(valor_com_taxa)
class ContaPoupanca(Conta):
    RENDIMENTO = 0.01

    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.RENDIMENTO