from src.ej1_def import saludo

def test_saludo():
    assert saludo("ivan") == "ivan"
    assert saludo("fran") == "fran"
    assert saludo("aroa") == "aroa"
