import pytest

from src.calculadora import dividir


def test_dividir_numeros_validos():
    assert dividir(10, 2) == 5.0

def test_dividir_por_zero_deve_falhar():
    with pytest.raises(ValueError):
        dividir(10, 0)