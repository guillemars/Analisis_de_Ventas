from analisis import calcular_total

def test_calcular_total():
    assert calcular_total(5, 10) == 50
    assert calcular_total(0, 100) == 0
    assert calcular_total(3, 0) == 0
