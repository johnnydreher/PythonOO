import pytest
from src.catalogo import Catalogo, Produto

def test_busca_e_ordenacao_produtos():
    c = Catalogo()
    c.adicionar(Produto("Mouse", 80.0))
    c.adicionar(Produto("Teclado", 50.0))
    c.adicionar(Produto("Monitor", 1200.0))
    p = c.buscar("Teclado")
    assert p is not None
    assert pytest.approx(p.preco, rel=1e-3) == 50.0
    ordenados = c.listar_ordenados_por_preco()
    assert ordenados[0].nome == "Teclado"
    assert ordenados[-1].nome == "Monitor"
