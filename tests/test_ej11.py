from src.ej11_def import calculo

def test_calcul():
    assert calculo(9) == 45
    assert calculo(4) == 10
    assert calculo(-5) == 10 
