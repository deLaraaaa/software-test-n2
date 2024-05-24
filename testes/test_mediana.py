from conftest import *
from stat_funcs import StatsN2
import pytest


def test_mediana(lista):
    res = StatsN2.mediana(lista)
    assert res == 2


def test_mediana_zero():
    res = StatsN2.mediana([])
    assert res == 0


def test_mediana_modulus():
    res = StatsN2.mediana([1, 2, 1, 1, 3])
    assert res == 1.0


@pytest.mark.xfail(reason="esperado falhar")
def test_mediana_fail(lista):
    res = StatsN2.mediana(lista)
    assert res == 1


@pytest.mark.parametrize("test_par,esperado", [
    ([1, 1, 2, 3], 1.75)
])
def test_mediana_par(test_par, esperado):
    res = StatsN2.mediana(test_par)
    assert res == 1.5

