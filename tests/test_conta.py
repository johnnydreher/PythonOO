import pytest
from src.conta import ContaCorrente, ContaPoupanca

def test_conta_corrente_saque():
    c = ContaCorrente(100)
    c.sacar(10)
    assert pytest.approx(c.get_saldo(), rel=1e-3) == 89.5

def test_conta_poupanca_rendimento():
    p = ContaPoupanca(200)
    p.aplicar_rendimento()
    assert pytest.approx(p.get_saldo(), rel=1e-3) == 202.0
