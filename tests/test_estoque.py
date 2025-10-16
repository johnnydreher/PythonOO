import pytest
from src.estoque import Estoque

def test_adicionar_e_remover_itens():
    e = Estoque()
    e.adicionar("parafuso", 50)
    e.adicionar("porca", 20)
    assert e.quantidade("parafuso") == 50
    assert e.quantidade("porca") == 20
    assert e.remover("parafuso", 10)
    assert e.quantidade("parafuso") == 40
    assert not e.remover("porca", 30)
    assert e.quantidade("porca") == 20
