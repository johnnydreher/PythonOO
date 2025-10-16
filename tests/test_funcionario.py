import pytest
from src.funcionario import FuncionarioCLT, FuncionarioPJ

def test_calculo_salario_funcionarios():
    f1 = FuncionarioCLT("Alice", 5000)
    f2 = FuncionarioPJ("Bob", 4000, 1500)
    assert pytest.approx(f1.calcular_salario(), rel=1e-3) == 6000
    assert pytest.approx(f2.calcular_salario(), rel=1e-3) == 5500
    assert f1.get_nome() == "Alice"
    assert f2.get_nome() == "Bob"
