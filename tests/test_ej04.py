from src.ej4_def2 import celsius_funcion

def test_celsius_funcion():
    assert celsius_funcion (30) == 22.00
    assert celsius_funcion (40) == 40.00
    assert celsius_funcion (-10) == -50.00
    assert celsius_funcion (0) == -32.00
