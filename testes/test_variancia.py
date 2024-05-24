from conftest import *
from stat_funcs import StatsN2
import pytest


def test_variancia(lista):
    res = StatsN2.variancia(lista)
    assert res == 0.6666666666666666


@pytest.mark.xfail(reason="esperado falhar")
def test_variancia_fail(lista):
    res = StatsN2.variancia(lista)
    assert res == 1


@pytest.mark.parametrize("lista_par,esperado", [
    ([1, 1, 2, 3], 2)
])
def test_variancia_par(lista_par, esperado):
    res = StatsN2.variancia(lista_par)
    assert res == 0.9166666666666666
