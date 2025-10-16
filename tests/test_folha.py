import pytest, re
from src.folha import Assalariado, Comissionado, FolhaPagamento

def test_calculo_salarios_individuais():
    a = Assalariado("João", 3200.0)
    c = Comissionado("Maria", 1500.0, 0.10, 20000.0)
    assert pytest.approx(a.calcular_salario(), rel=1e-3) == 3200.0
    assert pytest.approx(c.calcular_salario(), rel=1e-3) == 3500.0

def test_total_folha_pagamento():
    f = FolhaPagamento()
    f.adicionar(Assalariado("Ana", 2500.0))
    f.adicionar(Comissionado("Carlos", 2000.0, 0.10, 30000.0))
    assert pytest.approx(f.total(), rel=1e-3) == 7500.0

def test_relatorio_folha_pagamento():
    f = FolhaPagamento()
    f.adicionar(Assalariado("Carlos", 4000.0))
    f.adicionar(Comissionado("Julia", 2500.0, 0.05, 30000.0))
    rel = f.relatorio()
    assert "Carlos" in rel
    assert "Julia" in rel
    assert "Assalariado" in rel
    assert "Comissionado" in rel
    assert re.search(r"\b\d{3,5}(\.\d{1,2})?\b", rel)
    assert "4000" in rel
    assert "Total" in rel
    assert "8000" in rel
