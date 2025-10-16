import pytest
from src.biblioteca import Biblioteca, Livro, Revista

def test_adicao_e_listagem_de_publicacoes():
    b = Biblioteca()
    b.adicionar(Livro("C++ Moderno", "Bjarne", 350))
    b.adicionar(Revista("TechNow", "Vários", 42))
    lista = b.listar()
    assert "C++ Moderno" in lista
    assert "Edicao 42" in lista
    assert "Bjarne" in lista
    assert "Vários" in lista
