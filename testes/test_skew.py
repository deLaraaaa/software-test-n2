from conftest import *
from stat_funcs import StatsN2
import pytest


def test_skew(lista):
    res = StatsN2.skew(lista)
    assert res == "Distribuição normal"


def test_skew_negative():
    res = StatsN2.skew([1, 1, -10])
    assert res == "Distribuição negativa"


@pytest.mark.xfail(reason="esperado falhar")
def test_skew_fail(lista):
    res = StatsN2.skew(lista)
    assert res == "Distribuição negativa"


@pytest.mark.parametrize("lista_par,esperado", [
    ([1, 1, 2, 3], 2)
])
def test_skew_par(lista_par, esperado):
    res = StatsN2.skew(lista_par)
    assert res == "Distribuição positiva"
