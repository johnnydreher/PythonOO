"""
Enunciado:
Desenvolva um sistema de controle de estoque.

O sistema deve:
- Permitir adicionar itens com nome e quantidade.
- Permitir consultar a quantidade de um item específico.
- Permitir remover uma quantidade de um item.
- Retornar False se tentar remover mais do que o disponível.

O que será avaliado:
- Manipulação de dicionários ou listas.
- Controle de erros e retornos booleanos.
- Clareza de código e mensagens coerentes.
"""
# TODO: implementar classe Estoque
class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar(self, nome, quantidade):
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade

    def quantidade(self, nome):
        return self.itens.get(nome, 0)

    def remover(self, nome, quantidade):
        if nome in self.itens and self.itens[nome] >= quantidade:
            self.itens[nome] -= quantidade
            return True
        return False