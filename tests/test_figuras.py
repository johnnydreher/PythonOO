import pytest
import math
from src.figuras import Circulo, Retangulo

def test_area_circulo():
    c = Circulo(2.0)
    assert pytest.approx(c.area(), rel=1e-3) == math.pi * 4.0

def test_area_retangulo():
    r = Retangulo(5.0, 3.0)
    assert pytest.approx(r.area(), rel=1e-3) == 15.0
