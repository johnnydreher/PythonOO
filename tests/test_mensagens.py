import pytest
from src.mensagens import Mensageiro, Texto

def test_mensageiro_filtragem():
    m = Mensageiro()
    m.adicionar(Texto("oi mundo"))
    m.adicionar(Texto("tchau"))
    m.adicionar(Texto("oi de novo"))
    filtradas = m.filtrar_por_palavra("oi")
    assert len(filtradas) == 2
    assert all("oi" in msg for msg in filtradas)
    assert m.total() == 3
    vazias = m.filtrar_por_palavra("xyz")
    assert vazias == []
