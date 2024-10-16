from src.ej2_def import total_totalisimo

def test_total_totalisimo():

    assert total_totalisimo(6, 5) == 30
    assert total_totalisimo(10, 7) == 70
    assert total_totalisimo(-6, 5) == -30
    
