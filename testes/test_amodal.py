from conftest import *
from stat_funcs import StatsN2
import pytest


def test_amodal():
    res = StatsN2.amodal([1, 1, 2, 2, 3])
    assert res == "Existe moda"


def test_amodal_not():
    res = StatsN2.amodal([1, 2, 3])
    assert res == "Não existe moda"


@pytest.mark.xfail(reason="esperado falhar")
def test_amodal_fail():
    res = StatsN2.amodal([1, 1, 2, 2, 3])
    assert res == "Não existe moda"


@pytest.mark.parametrize("lista_par,esperado", [
    ([1, 1, 2, 3, 3], [1, 3])
])
def test_amodal_par(lista_par, esperado):
    res = StatsN2.amodal(lista_par)
    assert res == "Existe moda"
