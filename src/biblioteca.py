"""
Enunciado:
Crie um sistema para gerenciar publicações de uma biblioteca.

O sistema deve:
- Permitir adicionar publicações do tipo Livro e Revista.
- Cada Livro possui: título, autor e número de páginas.
- Cada Revista possui: título, autor e número da edição.
- A classe Biblioteca deve armazenar múltiplas publicações e oferecer:
  - adicionar(publicacao)
  - listar(): retorna uma string com os títulos, autores e edições/páginas de todas as publicações.

O que será avaliado:
- Uso de herança (Livro e Revista herdando de uma classe base, ex: Publicacao).
- Implementação do método polimórfico descricao() em cada tipo.
- Clareza e formatação na listagem.
"""
# TODO: implementar classes Publicacao, Livro, Revista e Biblioteca
class Publicacao:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        raise NotImplementedError("Subclasses devem implementar este método")
class Livro(Publicacao):
    def __init__(self, titulo, autor, num_paginas):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas

    def descricao(self):
        return f"Livro {self.titulo}, Autor {self.autor}, Paginas {self.num_paginas}"
class Revista(Publicacao):
    def __init__(self, titulo, autor, num_edicao):
        super().__init__(titulo, autor)
        self.num_edicao = num_edicao

    def descricao(self):
        return f"Revista {self.titulo}, Autor {self.autor}, Edicao {self.num_edicao}"
class Biblioteca:
    def __init__(self):
        self.publicacoes = []

    def adicionar(self, publicacao):
        self.publicacoes.append(publicacao)

    def listar(self):
        return "\n".join(pub.descricao() for pub in self.publicacoes)