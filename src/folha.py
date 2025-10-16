"""
Enunciado:
Crie um sistema de folha de pagamento com diferentes tipos de funcionários.

O sistema deve:
- Ter classes de funcionários:
  - Assalariado: recebe um valor fixo mensal.
  - Comissionado: recebe um valor base mais uma comissão sobre as vendas.
- Ter uma classe FolhaPagamento que:
  - Permite adicionar funcionários.
  - Calcula o total de salários com total().
  - Gera um relatório textual (relatorio()) com:
    - Nome, tipo e salário de cada funcionário.
    - Valor total da folha ao final.

O que será avaliado:
- Uso de herança e polimorfismo.
- Cálculo correto dos salários.
- Formatação e clareza do relatório.
"""
# TODO: implementar classes Assalariado, Comissionado e FolhaPagamento
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        raise NotImplementedError("Subclasses devem implementar este método")

    def tipo(self):
        raise NotImplementedError("Subclasses devem implementar este método") 
class Assalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal

    def tipo(self):
        return "Assalariado"
class Comissionado(Funcionario):
    def __init__(self, nome, salario_base, vendas, taxa_comissao):
        super().__init__(nome)
        self.salario_base = salario_base
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.taxa_comissao)

    def tipo(self):
        return "Comissionado"
class FolhaPagamento:
    def __init__(self):
        self.funcionarios = []

    def adicionar(self, funcionario):
        self.funcionarios.append(funcionario)

    def total(self):
        return sum(func.calcular_salario() for func in self.funcionarios)

    def relatorio(self):
        relatorio_texto = "Relatorio de Folha de Pagamento:\n"
        relatorio_texto += "-" * 40 + "\n"
        for func in self.funcionarios:
            relatorio_texto += f"Nome: {func.nome}, Tipo: {func.tipo()}, Salário: R$ {func.calcular_salario():.2f}\n"
        relatorio_texto += "-" * 40 + "\n"
        relatorio_texto += f"Total da Folha: R$ {self.total():.2f}\n"
        return relatorio_texto