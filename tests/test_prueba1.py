from src.prueba1 import retorna_mayor_numero
import pytest

def test_retornar_mayor_numero():
    assert retorna_mayor_numero (10,4) == 10
    assert retorna_mayor_numero (2,80) == 80
    assert retorna_mayor_numero (0,0) == 0
    assert retorna_mayor_numero (0,1) == 1

@pytest.mark.parametrize()