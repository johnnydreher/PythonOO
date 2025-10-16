"""
Enunciado:
Crie um sistema de catálogo de produtos com busca e ordenação.

O sistema deve:
- Permitir adicionar produtos com nome e preço.
- Fornecer uma função buscar(nome) que retorna o produto correspondente (ou None).
- Permitir listar todos os produtos ordenados pelo preço com listar_ordenados_por_preco().

O que será avaliado:
- Uso de classes e encapsulamento.
- Implementação correta da busca e da ordenação.
- Uso de listas, sort() e/ou lambda.
"""
# TODO: implementar classes Produto e Catalogo
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto(nome={self.nome}, preco={self.preco})"
class Catalogo:
    def __init__(self):
        self.produtos = []

    def adicionar(self, novo_produto):
        
        self.produtos.append(novo_produto)

    def buscar(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def listar_ordenados_por_preco(self):
        return sorted(self.produtos, key=lambda produto: produto.preco)