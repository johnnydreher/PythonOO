"""
Enunciado:
Crie um sistema simples de mensagens de texto.

O sistema deve:
- Ter uma classe Texto que representa uma mensagem (conteúdo textual).
- Ter uma classe Mensageiro que:
  - Armazena mensagens.
  - Permite adicionar novas mensagens (adicionar()).
  - Permite filtrar mensagens que contenham uma palavra específica (filtrar_por_palavra(palavra)).
  - Retorna o total de mensagens com total().

O que será avaliado:
- Manipulação de listas e strings.
- Implementação de filtros e buscas textuais.
- Clareza e legibilidade do código.
"""
# TODO: implementar classes Texto e Mensageiro
class Texto:
    def __init__(self, conteudo: str):
        self.conteudo = conteudo

    def __contains__(self, palavra: str):
        """Permite usar 'palavra in texto_objeto'."""
        return palavra in self.conteudo

    def __str__(self):
        """Quando convertido pra string."""
        return self.conteudo

class Mensageiro:
    def __init__(self):
        self.mensagens = []

    def adicionar(self, mensagem):
        if isinstance(mensagem, Texto):
            self.mensagens.append(mensagem)
        else:
            raise ValueError("A mensagem deve ser uma instância da classe Texto.")

    def filtrar_por_palavra(self, palavra):
        return [mensagem for mensagem in self.mensagens if palavra in mensagem.conteudo]

    def total(self):
        return len(self.mensagens)