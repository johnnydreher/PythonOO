import pytest
from src.sensores import SensorTemperatura, SensorPressao, SistemaMonitoramento

def test_leituras_dentro_intervalo():
    t = SensorTemperatura()
    p = SensorPressao()
    temp = t.ler()
    press = p.ler()
    assert 20.0 <= temp <= 30.0
    assert 950.0 <= press <= 1050.0

def test_relatorio_monitoramento():
    sys = SistemaMonitoramento()
    sys.adicionar(SensorTemperatura())
    sys.adicionar(SensorPressao())
    rel = sys.relatorio()
    assert "Temperatura" in rel
    assert "Pressão" in rel
