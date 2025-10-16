"""
Enunciado:
Implemente duas variações de funcionário para cálculo de pagamento.

O sistema deve:
- Ter uma classe base Funcionario com nome e salário base.
- Ter classes derivadas:
  - FuncionarioCLT: recebe um acréscimo fixo de 20% sobre o salário base.
  - FuncionarioPJ: recebe o salário base mais um bônus informado no construtor.
- Métodos obrigatórios:
  - calcular_salario()
  - get_nome()

O que será avaliado:
- Herança e sobrescrita de métodos.
- Clareza e simplicidade dos cálculos.
"""
# TODO: implementar classes Funcionario, FuncionarioCLT e FuncionarioPJ
class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        return self.salario_base

    def get_nome(self) -> str:
        return self.nome
class FuncionarioCLT(Funcionario):
    def calcular_salario(self) -> float:
        return self.salario_base * 1.2
class FuncionarioPJ(Funcionario):
    def __init__(self, nome: str, salario_base: float, bonus: float):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self) -> float:
        return self.salario_base + self.bonus